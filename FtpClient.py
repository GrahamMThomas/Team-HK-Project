from kivy.app import App

from LoginScreen import LoginScreen
from TransferScreen import TransferScreen

from Settings import *

sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(TransferScreen(name = 'transfer'))

class FtpClient(App):
	def build(self):
		return sm


if __name__ == '__main__':
	FtpClient().run()