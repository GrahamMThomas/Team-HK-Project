from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.app import App 
from kivy.core.window import Window  
from Settings import * 
from LoginScreen import LoginScreen 

Window.clearcolor = (.17,.17,.17,.5)
sm.add_widget(LoginScreen(name = 'login')) 

class Singleton:
	def __init__(self, decorated):
		self._decorated = decorated
	def Instance(self):
		try:
			return self._instance
		except AttributeError:
			self._instance = self._decorated()
			return self._instance
		def __call__(self):
			raise TypeError('Singletons must be accessed through Instance().')
		def __instanceCheck(self, inst):
			return isinstance(inst, self.decorated)
			
@Singleton
class FtpClient(App):
	def build(self): 
		return sm 

if __name__ == '__main__': 
	FtpApplicationRunner = FtpClient.Instance()
	FtpApplicationRunner.run()