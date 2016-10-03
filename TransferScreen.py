from kivy.uix.screenmanager import Screen

from HKftp import *
from kivy.uix.button import Button

class TransferScreen(Screen):

	def ListFiles(self, instance):
		self.connectButton.text = 'Pressed'
		HKftp.HKList()

	#TODO: Implement screen design

	def __init__(self, **kwargs):

		super(TransferScreen, self).__init__(**kwargs)

		self.connectButton = Button(text='Connect', on_press=self.ListFiles)
		self.add_widget(self.connectButton)