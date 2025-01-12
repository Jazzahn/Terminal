import npyscreen
import random
import requests
import time
import threading
from requests.adapters import HTTPAdapter

# gen1 = 0
# gen2 = 0
# gen3 = 0

# def worker1():
#     while True:
#         global gen1
#         s = requests.Session()
#         s.mount('http://10.1.20.60:5000/status', HTTPAdapter(max_retries=5))
#         gen1 = int(requests.get('http://10.1.20.60:5000/status').text)
#         time.sleep(2)

# def worker2():
#     while True:
#         global gen2
#         gen2 = int(requests.get('http://10.1.20.60:5000/tstatus').text)
#         time.sleep(2)

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
    F = LoginForm(name = 'XTEEN POWER INTERFACE 3.1.25')
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
#    npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
    while True:
        # n1 = 0
        # n2 = 0
        # n3 = 0
        F = npyscreen.Form(name = 'XTEEN POWER INTERFACE 3.1.25')
        t = F.add(npyscreen.FixedText, value = 'POWER FAILURE - RESTART GENERATORS 1, 2, and 3 TO RESTORE FULL POWER')
        F.nextrely += 1
        s = F.add(npyscreen.FixedText, value = 'GENERATOR 1 RESET')
        F.nextrely += 1
        s = F.add(npyscreen.FixedText, value = 'Press buttons labelled "O" at the same time and let go')
        F.nextrely += 1
        s = F.add(npyscreen.FixedText, value = " __________           _____ ")
        s = F.add(npyscreen.FixedText, value = "|          |         |     |")
        s = F.add(npyscreen.FixedText, value = "|  X    X  |         |  O  |")
        s = F.add(npyscreen.FixedText, value = "|      ____|         |_____|")
        s = F.add(npyscreen.FixedText, value = "|     |       ")
        s = F.add(npyscreen.FixedText, value = "|  O  |   ")
        s = F.add(npyscreen.FixedText, value = "|_____|  ")
        s = F.add(npyscreen.FixedText, value = " _____      _______________ ")
        s = F.add(npyscreen.FixedText, value = "|     |    |               |")
        s = F.add(npyscreen.FixedText, value = "|  X  |    |  X    O    X  |")
        s = F.add(npyscreen.FixedText, value = "|_____|    |_______________|")
        s = F.add(npyscreen.FixedText, value = " _____ ")
        s = F.add(npyscreen.FixedText, value = "|     |")
        s = F.add(npyscreen.FixedText, value = "|  X  |")
        s = F.add(npyscreen.FixedText, value = "|     |____           _____ ")
        s = F.add(npyscreen.FixedText, value = "|          |         |     |")
        s = F.add(npyscreen.FixedText, value = "|  X    O  |         |  X  |")
        s = F.add(npyscreen.FixedText, value = "|__________|         |_____|")
        
      
        F.display()
        #time.sleep(1)

if __name__ == "__main__":
    # n1 = threading.Thread(target=worker1)
    # n1.start()
    # n2 = threading.Thread(target=worker2)
    # n2.start()
    npyscreen.wrapper_basic(myFunction)