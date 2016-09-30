from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class TransferScreen(Screen):
	def __init__(self, **kwargs):

		super(TransferScreen, self).__init__(**kwargs)

		self.add_widget(Label(text='Screen 2'))