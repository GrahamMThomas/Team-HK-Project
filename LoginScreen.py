from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.screenmanager import Screen 


from TransferScreen import TransferScreen 
from Settings import * 
from HKftp import * 

class LoginScreen(GridLayout, Screen): 
	def ConnectUsingParameters(self, instance): 
		if self.host.text == '': #If no host is selected use default. 
			self.SetDefaultParameters(self) 
		ftpResultOfConnecting = FTPConnectionService.ConnectToFtpServer(self.host.text, self.port.text, self.username.text, self.password.text)
		if ftpResultOfConnecting: 
			self.SwitchToTransferScreen() 
			
	@staticmethod 
	def SwitchToTransferScreen(): 
		print "Switching to Transfer Screen..." 
		transferScreen = TransferScreen(name='transfer') 
		transferScreen.OnSwitch() 
		sm.add_widget(transferScreen) 
		sm.current = 'transfer' 


	def SetDefaultParameters(self, instance): 
		self.host.text = 'localhost' 
		self.port.text = '21' 
		self.username.text = 'IEUser' 
		self.password.text = 'test' 

	def __init__(self, **kwargs):
        #TODO: Separate these elements into a nicer format
		super(LoginScreen, self).__init__(**kwargs) 
		self.cols = 2
		
		self.add_widget(Label(text = "FTP", font_size = 40, size_hint_x = .8, color=(0,0,.7,1)))
		self.add_widget(Label(text = "APPLICATION", font_size = 40, size_hint_x = .8, color=(0,0,.7,1)))
		
		self.add_widget(Label(text='Host', size_hint_y = .2))
		self.host = TextInput(multiline=False)
		self.add_widget(self.host)
		
		self.add_widget(Label(text='Port'))
		self.port = TextInput(multiline=False)
		self.port.text = '21'
		self.add_widget(self.port)
		
		self.add_widget(Label(text='User Name'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		
		self.add_widget(Label(text='Password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)
		
		
		# Creating Connect Button
		self.output = Label()
		self.add_widget(self.output)
		self.add_widget(Label(text = " "))
		connectButton = Button(text='Connect')
		connectButton.bind(on_press=self.ConnectUsingParameters)
		self.add_widget(connectButton)
