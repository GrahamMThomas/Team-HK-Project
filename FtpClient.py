from kivy.app import App 
from kivy.core.window import Window 
 
from Settings import * 
from LoginScreen import LoginScreen 
from kivy.config import Config

Window.clearcolor = (.17,.17,.17,.5)
Config.set('input', 'mouse', 'mouse,disable_multitouch')

#TODO: Find a way to move these out of the main 
sm.add_widget(LoginScreen(name = 'login')) 
 

class FtpClient(App): 
	def build(self): 
		return sm 
 

if __name__ == '__main__': 
	FtpClient().run() 
