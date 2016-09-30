from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '140')
Config.set('graphics', 'borderless', '1')

#TODO: Find a way to not keep the screen manager in the config file.
sm = ScreenManager()