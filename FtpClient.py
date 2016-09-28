from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.button import Button
from ftplib import FTP


class LoginScreen(GridLayout):

	def ConnectUsingParameters(self, instance):
		self.output.text = "Connecting..."
		try:
			ftp = FTP(self.host.text)
			messageReceived = ftp.login(self.username.text, self.password.text)
			print "FTP returned: {}".format(messageReceived)
		except Exception, e:
			print "[ERROR] FTP connection failed with error: {}".format(e)

	def ConnectUsingDefaultParameters(self, instance):
		self.output.text = "Connecting..."
		try:
			ftp = FTP('localhost')
			messageReceived = ftp.login('IEUser', 'test')
			print "FTP returned: {}".format(messageReceived)
		except Exception, e:
			print "[ERROR] FTP connection failed with error: {}".format(e)

	def __init__(self, **kwargs):
		#Set the login screen size
		Config.set('graphics', 'width', '400')
		Config.set('graphics', 'height', '150')

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

class FtpClient(App):

	def build(self):
		return LoginScreen()


if __name__ == '__main__':
	FtpClient().run()