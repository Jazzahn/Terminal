import npyscreen
import requests
import time

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

def getPhase():
    n = 0
    r = requests.get('http://10.1.20.230/status')
    if r.text == 'phase one not triggered :: phase two not triggered':
        n = 0
    elif r.text == 'phase one triggered :: phase two not triggered':
        n = 1
    elif r.text == 'phase one triggered :: phase two triggered':
        n = 2
    return n

def getGen2Phase():
    n = 0
    r = requests.get('http://10.1.20.60/tstatus').text
    if r == 'Gen2: 000':
        n = 0
    elif r == 'Gen2: 025':
        n = 1
    elif r == 'Gen2: 050':
        n = 2
    elif r == 'Gen2: 075':
        n = 3
    elif r == 'Gen2: 100':
        n = 4
    return n

def myFunction(*args):
    F = LoginForm(name = 'XTEEN POWER INTERFACE 2.3.11')
    F.edit()
    if F.Login.value == '161803':
        F = PasswordCorrect()
        F.edit()
        n = 0
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
        n1 = getPhase()
        n2 = request.get('http://10.1.20.60/tstatus').text
        F = npyscreen.Form(name = 'XTEEN POWER INTERFACE 2.3.11')
        t = F.add(npyscreen.FixedText, value = 'POWER FAILURE - RESTART GENERATORS 1, 2, and 3 TO RESTORE FULL POWER')
        F.nextrely += 2
        s = F.add(npyscreen.TitleSlider, value = n1, out_of=2, name = 'GENERATOR 1', label = False)
        F.nextrely += 1
        s = F.add(npyscreen.TitleSlider, value = n2, out_of=4, name = 'GENERATOR 2', label = False)
        F.nextrely += 1
        s = F.add(npyscreen.TitleSlider, value = n3, out_of=2, name = 'GENERATOR 3', label = False)
        F.nextrely += 2
        t2 = F.add(npyscreen.FixedText, value = 'GENERATOR 1 PHASE 1 CODE: "if i cannot inspire Love, i will cause Fear"')
        F.nextrely += 1
        t3 = F.add(npyscreen.FixedText, value = 'GENERATOR 1 PHASE 2 CODE: "th0re ishjZhGtbNMUD6ZVa3  1/ecJPLXhEd7ogH bmJPFHKQV1xCMIi/qB/S    1IkzV+NVi0UhM')
        t5 = F.add(npyscreen.FixedText, value = 'Dkp+EyjyxSo10EFLPYw3cI1bohMTEhITMzISE   zNCFOl/sQqjCItW/G3o3WMSExMyFaGD4  skSUVNRDXdVkGfMTc8p12Vu')
        t5 = F.add(npyscreen.FixedText, value = 'ubnl1bUmKdMJV9NiSEzOSE5ykQDV  E/S0zzle/WljXO9y2aQ3a/Uk56S/SNApbrrdfiDA+5HK9c   GrbP34dPhff80GyaiT')
        F.nextrely += 2
        t4 = F.add(npyscreen.FixedText, value = 'ERROR TERMINAL MALFUNCTION - ERROR CODE 0x0045')
        F.display()
        time.sleep(1)
    
   
    #return F.Login.value
   #def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        #F  = npyscreen.Form(name = "XTeen Computer Interface",)
        #t  = F.add(npyscreen.TitleText, name = "LOGIN:",)
        #fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        #fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        #dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        #s  = F.add(npyscreen.TitleSlider, step=1 ,out_of=1, name = "GENERATOR 1")
        #ml = F.add(npyscreen.MultiLineEdit,
        #       value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
        #       max_height=5, rely=9)
        #ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
        #        values = ["Option1","Option2","Option3"], scroll_exit=True)
        #ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
        #        values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        
        #F.edit()

if __name__ == "__main__":
    #App = TestApp()
    #App.run()

    npyscreen.wrapper_basic(myFunction)