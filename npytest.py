import npyscreen
import requests
import time
import threading
from requests.adapters import HTTPAdapter

gen1 = 0
gen2 = 0
gen3 = 0

def worker1():
    while True:
        global gen1
        s = requests.Session()
        s.mount('http://10.1.20.60:5000/status', HTTPAdapter(max_retries=5))
        gen1 = int(requests.get('http://10.1.20.60:5000/status').text)
        time.sleep(2)

def worker2():
    while True:
        global gen2
        gen2 = int(requests.get('http://10.1.20.60:5000/tstatus').text)
        time.sleep(2)

class LoginForm(npyscreen.Form):
   def create(self):
        self.Login = self.add(npyscreen.TitleText, name = 'ENTER PASSWORD', rely=19, use_two_lines=False)
        self.Hint = self.add(npyscreen.TitleText, name= 'Password Hint: She was my greatest failure, I left her in the darkness', editable=False)

class PasswordCorrect(npyscreen.Popup):
    def create(self):
        self.Password = self.add(npyscreen.TitleText, name = ' ', value = 'PASSWORD CORRECT', editable=False)

class PasswordIncorrect(npyscreen.Popup):
    def create(self):
        self.Password = self.add(npyscreen.TitleText, name = ' ', value = 'PASSWORD INCORRECT', editable=False)        

def myFunction(*args):
    F = LoginForm(name = 'XTEEN POWER INTERFACE 2.3.11')
    F.edit()
    if F.Login.value == '161803':
        F = PasswordCorrect()
        F.edit()
        #n = 0
        npyscreen.wrapper_basic(mainScreen)
    elif F.Login.value != '161803':
        F = PasswordIncorrect()
        F.edit()
        npyscreen.wrapper_basic(myFunction)

def mainScreen(*args):
    while True:
        n1 = 0
        n2 = 0
        n3 = 0
        F = npyscreen.Form(name = 'XTEEN POWER INTERFACE 2.3.11')
        t = F.add(npyscreen.FixedText, value = 'POWER FAILURE - RESTART GENERATORS 1, 2, and 3 TO RESTORE FULL POWER')
        F.nextrely += 2
        s = F.add(npyscreen.TitleSlider, value = gen1, out_of=2, name = 'GENERATOR 1', label = False)
        F.nextrely += 1
        s = F.add(npyscreen.TitleSlider, value = gen2, out_of=4, name = 'GENERATOR 2', label = False)
        F.nextrely += 1
        s = F.add(npyscreen.TitleSlider, value = n3, out_of=2, name = 'GENERATOR 3', label = False)
        F.nextrely += 2
        t6 = F.add(npyscreen.FixedText, value = 'SECURITY CODE: 867-5309')
        F.nextrely += 1
        t2 = F.add(npyscreen.FixedText, value = 'GENERATOR 1 PHASE 1 CODE: "if i cannot inspire Love, i will cause Fear"')
        F.nextrely += 1
        t3 = F.add(npyscreen.FixedText, value = 'GENERATOR 1 PHASE 2 CODE: "th0re ishjZhGtbNMUD6ZVa3  1/ecJPLXhEd7ogH bmJPFHKQV1xCMIi/qB/S    1IkzV+NVi0UhM')
        t5 = F.add(npyscreen.FixedText, value = 'Dkp+EyjyxSo10EFLPYw3cI1bohMTEhITMzISE   zNCFOl/sQqjCItW/G3o3WMSExMyFaGD4  skSUVNRDXdVkGfMTc8p12Vu')
        t5 = F.add(npyscreen.FixedText, value = 'ubnl1bUmKdMJV9NiSEzOSE5ykQDV  E/S0zzle/WljXO9y2aQ3a/Uk56S/SNApbrrdfiDA+5HK9c   GrbP34dPhff80GyaiT')
        F.nextrely += 2
        t4 = F.add(npyscreen.FixedText, value = 'ERROR TERMINAL MALFUNCTION - ERROR CODE 0x0045')
        F.display()
        #time.sleep(1)

if __name__ == "__main__":
    n1 = threading.Thread(target=worker1)
    n1.start()
    n2 = threading.Thread(target=worker2)
    n2.start()
    npyscreen.wrapper_basic(myFunction)