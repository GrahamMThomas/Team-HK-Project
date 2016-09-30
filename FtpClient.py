from kivy.app import App

from Settings import *
from LoginScreen import LoginScreen
from TransferScreen import TransferScreen

#TODO: Find a way to move these out of the main
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(TransferScreen(name = 'transfer'))

class FtpClient(App):
	def build(self):
		return sm


if __name__ == '__main__':
	FtpClient().run()