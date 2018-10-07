import npyscreen
import requests
import time

class LoginForm(npyscreen.Form):
   def create(self):
        self.Login = self.add(npyscreen.TitleText, name = 'ENTER PASSWORD', rely=19, use_two_lines=False)

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
        n = 0
        npyscreen.wrapper_basic(mainScreen)
    elif F.Login.value != '161803':
        F = PasswordIncorrect()
        F.edit()
        npyscreen.wrapper_basic(myFunction)

def mainScreen(*args):
    n = 0
    r = requests.get('http://10.1.20.230/status')
    F = npyscreen.Form(name = 'XTEEN POWER INTERFACE 2.3.11')
    if r.text == 'phase one not triggered :: phase two not triggered':
        n = 0
    elif r.text == 'phase one triggered :: phase two not triggered':
        n = 1
    elif r.text == 'phase one triggered :: phase two triggered':
        n = 2
    s = F.add(npyscreen.TitleSlider, value = n, out_of=2, name = 'GENERATOR 1')
    F.display()
    time.sleep(1)
    mainScreen()
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