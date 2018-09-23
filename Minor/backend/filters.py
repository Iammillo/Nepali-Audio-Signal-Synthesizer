from scipy.io import wavfile
import numpy as np
import sounddevice as sd

def filter(x):
    sample_size=10
    threshold=1000
    count=0
    size=len(x)
    final_audio=[]
    for i in range(1,size):
        final_audio.append(x[i])
        if abs(x[i]) < threshold:
            count =count+1
            end=False
        else:
            end=True

        if count>sample_size and end==True :
            for j in range(1,count):
                final_audio.pop()
            count=0
        if end==True:
            count=0

    return final_audio

def smoothing(x):
    beta=0.98
    total_data=[]
    data=0
    for i in range(1,len(x)):
        data=data*beta + (1-beta)*x[i]
        data=int(data)
        total_data.append(data)
    return total_data
