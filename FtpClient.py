from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.button import Button
from ftplib import FTP
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(GridLayout,Screen):

	def ConnectUsingParameters(self, instance):
		self.output.text = "Connecting..."
		try:
			ftp = FTP()
			ftp.connect(self.host.text,self.port.text)
			messageReceived = ftp.login(self.username.text, self.password.text)
			print "FTP returned: {}".format(messageReceived)
			sm.current = 'transfer'
		except Exception, e:
			print "[ERROR] FTP connection failed with error: {}".format(e)

	def ConnectUsingDefaultParameters(self, instance):
		self.output.text = "Connecting..."
		try:
			ftp = FTP()
			ftp.connect('localhost','21')
			messageReceived = ftp.login('IEUser', 'test')
			print "FTP returned: {}".format(messageReceived)
			sm.current = 'transfer'
		except Exception, e:
			print "[ERROR] FTP connection failed with error: {}".format(e)

	def __init__(self, **kwargs):
		#TODO: Seperate these elements into a nicer format

		#Set the login screen size

		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2
		
		#Creating Host Field
		self.add_widget(Label(text='Host'))
		self.host = TextInput(multiline=False)
		self.add_widget(self.host)
		
		#Creating Port Field
		self.add_widget(Label(text='Port'))
		self.port = TextInput(multiline = False)
		self.add_widget(self.port)

		#Creating Username Field
		self.add_widget(Label(text='User Name'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		#Creating Password Field
		self.add_widget(Label(text='Password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)

		
		#Creating Connect Button
		self.output = Label()
		self.add_widget(self.output)
		connectButton = Button(text='Connect')
		connectButton.bind(on_press=self.ConnectUsingDefaultParameters)
		self.add_widget(connectButton)

class TransferScreen(Screen):
	def __init__(self, **kwargs):

		super(TransferScreen, self).__init__(**kwargs)

		self.add_widget(Label(text='Screen 2'))
		self.host = TextInput(multiline=False)
		self.add_widget(self.host)


sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(TransferScreen(name = 'transfer'))

class FtpClient(App):

	def build(self):
		return sm


if __name__ == '__main__':
	FtpClient().run()