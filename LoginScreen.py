from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.button import Button
from ftplib import FTP
from kivy.uix.screenmanager import ScreenManager, Screen
from time import sleep

from Settings import *

class LoginScreen(GridLayout, Screen):
    def ConnectUsingParameters(self, instance):
        self.output.text = "Connecting..."
        try:
            ftp = FTP()
            ftp.connect(self.host.text, int(self.port.text))
            messageReceived = ftp.login(self.username.text, self.password.text)
            print "FTP returned: {}".format(messageReceived)
            self.output.text = 'Connected.'
            sleep(2)
            sm.current = 'transfer'
        except Exception, e:
            print "[ERROR] FTP connection failed with error: {}".format(e)

    def ConnectUsingDefaultParameters(self, instance):
        self.host.text = 'localhost'
        self.port.text = '21'
        self.username.text = 'IEUser'
        self.password.text = 'test'
        self.ConnectUsingParameters(self)

    def __init__(self, **kwargs):
        #TODO: Seperate these elements into a nicer format

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
        connectButton.bind(on_press=self.ConnectUsingDefaultParameters)
        self.add_widget(connectButton)