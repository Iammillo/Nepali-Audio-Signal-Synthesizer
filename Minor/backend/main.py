import scipy.io.wavfile as wv
import numpy as np
import sounddevice as sd
import os
import scipy
from .filters import filter,smoothing

class engine:
    def text_entry(self,text):
        self.B = text

    def play(self):
        f = open(os.path.join(os.path.dirname(__file__),'mapping.txt'));
        data = f.read();
        data = data.split();
        A = self.B;
        count =0;
        charset =[];
        letters = ["क", "ख", "ग", "घ", "ड॒", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ" ,"द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह"]
        vowels = [ "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ"]
        other =['्','ा','ि','ी','ु','ू','े','ै','ो','ौ'];

        for m in A:
            if m not in letters and m not in vowels and m not in other and m !=" ":
                A = A.replace(m,"")

        while count < len(A):
            t1 = A[count];
            if count == len(A)-1:
                t2='space';
            else:
                t2 = A[count+1];
            if t1 ==' ':
                charset.append(1);
                count = count+1;
            elif t1 in vowels:
                temp = data.index(str(t1));
                charset.append(temp+1);
                count = count+1;
            elif t2 in other:
                text = str(t1)+str(t2);
                temp = data.index(text);
                charset.append(temp+1);
                count = count+2;
            elif t2==' ':
                text = str(t1)+other[0];
                temp = data.index(text);
                charset.append(temp+1);
                count = count+1;
            else:
                text = str(t1);
                temp = data.index(text);
                charset.append(temp+1);
                count = count+1;

        s = np.array([1]);
        s.reshape(1,1);
        print(charset);
        for i in charset:
            sr,y = wv.read(os.path.join(os.path.dirname(__file__),'data/'+str(i)+'.wav'));
            y.reshape(len(y),1);
            s = np.concatenate((s,y))

        sd.play(s.astype(np.int16),sr)
        sd.wait();
        wv.write(os.path.join(os.path.dirname(__file__),'data.wav'),sr,s.astype(np.int16))
