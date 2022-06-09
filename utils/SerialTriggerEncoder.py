import os
import argparse
from scipy.io.wavfile import write
import numpy as np

class SerialTriggerEncoder:
    """
    Serial Trigger encoder for EEG recording

    ...

    Attributes
    ----------
    fsAudio : int
        sampling rate of trigger as an audio output
    clkSerial : int
        the clock rate of trigger

    Methods
    -------
    encode(code, time, **kwargs)
    resetTrigger()
    generateTrigger(out_path, length)
    """

    def __init__(self, fsAudio, clkSerial):
        self.__fsAudio = fsAudio
        self.__clkSerial = clkSerial
        self.__nHalfPeriod = round(self.__fsAudio/self.__clkSerial/2)
        self.__series = []

    @property
    def fsAudio(self):
        return self.__fsAudio
    @fsAudio.setter
    def fsAudio(self, newFsAudio):
        self.__fsAudio = newFsAudio
    
    @property
    def clkSerial(self):
        return self.__clkSerial
    @clkSerial.setter
    def clkSerial(self, newClkSerial):
        self.__clkSerial = newClkSerial

    def encode(self, code, time, **kwargs):
        for key, value in kwargs.items():
            if key=='fsAudio':
                self.__fsAudio = value
            if key=='clkSerial':
                self.__clkSerial = value
        self.__nHalfPeriod = round(self.__fsAudio/self.__clkSerial/2)
        triggerStr = bin(code).replace("0b", "")
        triggerSeq = []
        triggerSeq = triggerSeq + ([1]*self.__nHalfPeriod)
        triggerSeq = triggerSeq + ([-1]*self.__nHalfPeriod) # default first bit for starting a trigger
        for dg in triggerStr:
            if dg=='0':
                triggerSeq = triggerSeq + ([1]*self.__nHalfPeriod)
                triggerSeq = triggerSeq + ([-1]*self.__nHalfPeriod)
            elif dg=='1':
                triggerSeq = triggerSeq + ([-1]*self.__nHalfPeriod)
                triggerSeq = triggerSeq + ([1]*self.__nHalfPeriod)

        triggerData = {
            "time": time,
            "value": code,
            "seq": triggerSeq
        }
        self.__series.append(triggerData)

    def resetTrigger(self):
        del self.__series[:]
    
    def generateTrigger(self, out_path, length, samplewidth=2, nchannels=1):
        filename, file_extension = os.path.splitext(out_path)
        meta_filename = filename + ".txt"

        if samplewidth==2:
            packtype = 'h'
        elif samplewidth > 4:
            print('Not supporting samplewidth greater than 4.')
            exit()
        else:
            packtype = 'i'

        num_samples =   int(length*self.__fsAudio)
        num_pulses = len(self.__series)
        audio = [0]*num_samples
        meta_file = open(meta_filename, 'w')
        for i in range(num_pulses):
            time = self.__series[i]['time']
            if time < length:
                triggerSeq = self.__series[i]['seq']
                startSample = int(time*self.__fsAudio)
                audio[startSample:startSample+len(triggerSeq)] = triggerSeq
                meta_file.write("{}\n".format(self.__series[i]['value']))
        if not meta_file.closed:
            meta_file.close()

        write(out_path, self.__fsAudio, (32767*np.array(audio)).astype(np.int16))
