import npyscreen
import requests
import time

class LoginForm(npyscreen.Form):
   def create(self):
        self.Login = self.add(npyscreen.TitleText, name = 'LOGIN')

class PasswordCorrect(npyscreen.Popup):
    def create(self):
        self.Password = self.add(npyscreen.TitleText, name = ' ', value = 'PASSWORD CORRECT', editable=False)

class PasswordIncorrect(npyscreen.Popup):
    def create(self):
        self.Password = self.add(npyscreen.TitleText, name = ' ', value = 'PASSWORD INCORRECT', editable=False)        


def myFunction(*args):
    F = LoginForm(name = 'XTEEN POWER INTERFACE')
    F.edit()
    if F.Login.value == '161200':
        F = PasswordCorrect()
        F.edit()
        n = 0
        npyscreen.wrapper_basic(mainScreen)
    elif F.Login.value != '161200':
        F = PasswordIncorrect()
        F.edit()
        npyscreen.wrapper_basic(myFunction)

def mainScreen(*args):
    n = 0
    r = requests.get('http://10.1.20.230/status')
    F = npyscreen.Form(name = 'XTeen Computer Interface')
    if r.text == 'Phase One Not Triggered :: Phase Two Not Triggered':
        n = 0
    elif r.text == 'Phase One Triggered :: Phase Two Not Triggered':
        n = 1
    s = F.add(npyscreen.TitleSlider, value = n, out_of=2, name = 'GENERATOR 1')
    while n < 3:
        F.display()
        time.sleep(2)
        pass
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