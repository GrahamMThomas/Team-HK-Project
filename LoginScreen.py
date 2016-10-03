from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from Settings import *
from HKftp import *

class LoginScreen(GridLayout, Screen):
    def ConnectUsingParameters(self, instance):
        if self.host.text == '':
            self.SetDefaultParameters(self)
        self.output.text = "Connecting..."
        ftpResult = HKftp.HKConnect(self.host.text, self.port.text, self.username.text, self.password.text)
        if ftpResult:
            sm.current = 'transfer'

    def SetDefaultParameters(self, instance):
        self.host.text = 'localhost'
        self.port.text = '21'
        self.username.text = 'IEUser'
        self.password.text = 'test'

    def __init__(self, **kwargs):
        #TODO: Separate these elements into a nicer format

        # Set the login screen size
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        # Creating Host Field
        self.add_widget(Label(text='Host'))
        self.host = TextInput(multiline=False)
        self.add_widget(self.host)

        # Creating Port Field
        self.add_widget(Label(text='Port'))
        self.port = TextInput(multiline=False)
        self.port.text = '21'
        self.add_widget(self.port)

        # Creating Username Field
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Creating Password Field
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        # Creating Connect Button
        self.output = Label()
        self.add_widget(self.output)
        connectButton = Button(text='Connect')
        connectButton.bind(on_press=self.ConnectUsingParameters)
        self.add_widget(connectButton)