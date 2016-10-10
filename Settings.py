from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config


Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '140')
Config.set('graphics', 'borderless', '0')

#TODO: Stop using global variables like a noob.

sm = ScreenManager()