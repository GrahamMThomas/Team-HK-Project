from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class TransferScreen(Screen):
	def __init__(self, **kwargs):

		super(TransferScreen, self).__init__(**kwargs)

		self.add_widget(Label(text='Screen 2'))
		self.host = TextInput(multiline=False)
		self.add_widget(self.host)