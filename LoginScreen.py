from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.screenmanager import Screen 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.actionbar import *

import time
import datetime

from TransferScreen import TransferScreen 
from Settings import * 
from HKftp import * 

def closeErrorPopupLogin(self):
	errorPopupLogin.dismiss()

popupBoxLayout = BoxLayout(orientation = 'vertical')
errorInformationMessage = Label(text = "Information Not Filled", font_size = 20)
confirmationInformationButton = Button(text = "OK", size_hint_y = .4, on_release = closeErrorPopupLogin)
popupBoxLayout.add_widget(errorInformationMessage)
popupBoxLayout.add_widget(confirmationInformationButton)
errorPopupLogin = Popup(title = "Error: INFORMATION", content = popupBoxLayout, size_hint = (.5, .4))

class LoginScreen(GridLayout, Screen): 
	def ConnectUsingParameters(self, instance): 	
		
		if self.host.text == '': #If no host is selected use default. 
			self.host.background_color = (1,.2,.2,1)
		else:
			self.host.background_color = (1,1,1,1)
			
		if self.port.text == '':
			self.port.background_color = (1,.2,.2,1)
		else:
			self.port.background_color = (1,1,1,1)
		
		if self.username.text == '':
			self.username.background_color = (1,.2,.2,1)
		else:
			self.username.background_color = (1,1,1,1)
		
		if self.password.text == '':
			self.password.background_color = (1,.2,.2,1)
		else:
			self.password.background_color = (1,1,1,1)
	
		if self.host.text != '' and self.port.text != '' and self.username.text != '' and self.password.text != '':
			ftpResultOfConnecting = FTPConnectionService.ConnectToFtpServer(self.host.text, self.port.text, self.username.text, self.password.text)	
			if (ftpResultOfConnecting):
				self.actionToggleButton.background_color = (0,1,0,1)
				self.actionToggleButton.opacity = 1
				self.SwitchToTransferScreen()
			else:
				errorInformationMessage.text = "Failed to connect"
				errorPopupLogin.title = "Error: No CONNECTION"
				errorPopupLogin.open()
		else:
			errorInformationMessage.text = "Information not Filled"
			errorPopupLogin.title = "Error: EMPTY Fields"
			errorPopupLogin.open()
								
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
		self.password.text = 'Passw0rd!'
	
	def __init__(self, **kwargs):
        #TODO: Separate these elements into a nicer format
		super(LoginScreen, self).__init__(**kwargs) 
		self.cols = 1
		
		self.actionBar = ActionBar()
		self.actionView = ActionView()
		self.copyRightSymbol = u"\u00A9"
		self.actionPrevious = ActionPrevious(title = "TeamHK " + self.copyRightSymbol, with_previous = False, app_icon = "", app_icon_width = 1, app_icon_height = 0)
		
		self.actionToggleButton = ActionToggleButton(text = "CONNECTED", group = "ONLY", state = 'down', allow_selection = False,background_color = (1,.2,.2,1), disabled = True, color = (1,.2,.2,1), opacity = 2)
		self.actionView.add_widget(self.actionPrevious)
		self.defaultButton = ActionButton(text = "DEFAULT", on_press = self.SetDefaultParameters)
		self.actionView.add_widget(self.defaultButton)
		self.actionView.add_widget(self.actionToggleButton)

		self.date_time = str(datetime.datetime.now())
		self.Date = self.date_time.split()[0]
		self.Date = datetime.datetime.now().strftime("%m") +  datetime.datetime.now().strftime("-%d") + datetime.datetime.now().strftime("-%Y") 
		self.actionButtonCurrentDate = ActionButton(text = self.Date)
		self.actionView.add_widget(self.actionButtonCurrentDate)
		
		self.actionBar.add_widget(self.actionView)
		self.add_widget(self.actionBar)
		
		self.boxlayoutApplicationHeader = BoxLayout(padding = [20,0,0,20],orientation = "vertical",cols = 1)
		self.boxlayoutApplicationHeader.add_widget(Label(text = "FTP APPLICATION", font_size = 50, bold = True, color=(.01,.973,.99,1)))
		self.add_widget(self.boxlayoutApplicationHeader)
		
		self.boxlayoutHost = BoxLayout(padding = [250,24],orientation = "vertical",cols = 1)
		self.host = TextInput(hint_text = "Host", multiline=False, cursor_color = (0,0,1,1), write_tab = False)
		self.boxlayoutHost.add_widget(self.host)
		self.add_widget(self.boxlayoutHost)
		
		self.boxlayoutPort = BoxLayout(padding = [250,23],orientation = "vertical",cols = 1)
		self.port = TextInput(hint_text = "Port", multiline=False, cursor_color = (0,0,1,1), input_filter = 'int', write_tab = False)
		self.boxlayoutPort.add_widget(self.port)
		self.add_widget(self.boxlayoutPort)
		
		self.boxlayoutUserName = BoxLayout(padding = [250,23],orientation = "vertical",cols = 1)
		self.username = TextInput(hint_text = "Username", multiline=False, cursor_color = (0,0,1,1), write_tab = False)
		self.boxlayoutUserName.add_widget(self.username)
		self.add_widget(self.boxlayoutUserName)
		
		self.boxlayoutPassword = BoxLayout(padding = [250,25],orientation = "vertical",cols = 1)
		self.password = TextInput(hint_text = "Password", multiline=False, password = True, allow_copy = False, cursor_color = (0,0,1,1), write_tab = False)
		self.boxlayoutPassword.add_widget(self.password)
		self.add_widget(self.boxlayoutPassword)
		
		self.boxlayoutConnect = BoxLayout(padding = [280,25],orientation = "vertical",cols = 1)
		self.connectButton = Button(text='Connect', font_size = 20, background_color = (.01,.973,.99,1))
		self.connectButton.bind(on_press=self.ConnectUsingParameters)
		self.boxlayoutConnect.add_widget(self.connectButton)
		self.add_widget(self.boxlayoutConnect)				