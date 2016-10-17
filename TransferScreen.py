from kivy.uix.gridlayout import GridLayout 
from kivy.uix.screenmanager import Screen 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.uix.label import Label 
from kivy.adapters.dictadapter import ListAdapter 
from kivy.uix.listview import ListView, ListItemButton 


from Settings import * 
from HKftp import * 
from kivy.uix.button import Button 
 
class TransferScreen(GridLayout, Screen): 
	def ListFiles(self, instance = None): 
		#TODO: Add formatting here 
		return HKftp.FtpListCommand() 
 
 	def OnSwitch(self): 
		#TODO: Add more method needed on screen switch 
		self.SetClientList() 
		
 	def SetClientList(self): 
		output = self.ListFiles() 
		list_adapter = ListAdapter(data=["{}".format(i) for i in output], cls=ListItemButton, sortedKeys=[]) 
		list_view = ListView(adapter=list_adapter) 
		self.add_widget(list_view) 

 	#TODO: Implement screen design 
 	def __init__(self, **kwargs): 
		super(TransferScreen, self).__init__(**kwargs) 
		
		self.cols = 2 
		self.label = Label(size_hint_y=None, height=50) 
		self.add_widget(self.label) 
		
		self.listButton = Button(text='List Files', on_press=self.ListFiles, size_hint_y=None, height = 50) 
		self.add_widget(self.listButton) 
 
		self.fileChooser = FileChooserIconView(path="C:\\Users\\IEUser\\Desktop\\") 
		self.add_widget(self.fileChooser) 
