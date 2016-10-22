from kivy.uix.gridlayout import GridLayout 
from kivy.uix.screenmanager import Screen 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.uix.label import Label 
from kivy.adapters.dictadapter import ListAdapter 
from kivy.uix.listview import ListView, ListItemButton 


from Settings import * 
from HKftp import * 
from kivy.uix.button import Button 

# FIXME: All the global need to go away.
UPLOADBUTTON = Button()
DOWNLOADBUTTON = Button()
LISTVIEW = ListView()

class TransferScreen(GridLayout, Screen): 
	def ListFiles(self, instance = None): 
		#TODO: Add formatting here 
		return FTPConnectionService.FtpListCommand()

	def ReAddButtons(self,instance = None):
		global UPLOADBUTTON
		global DOWNLOADBUTTON

		UPLOADBUTTON = Button(text='>>>>', on_press=self.ListFiles, size_hint_y=None, height=50)
		self.add_widget(UPLOADBUTTON)

		DOWNLOADBUTTON = Button(text='<<<<', on_press=self.ListFiles, size_hint_y=None, height=50)
		self.add_widget(DOWNLOADBUTTON)

	def UpdateFtpDirectoryListing(self, instance = None):
		global LISTVIEW
		global UPLOADBUTTON
		global DOWNLOADBUTTON
		# Removing old widgets
		self.remove_widget(UPLOADBUTTON)
		self.remove_widget(DOWNLOADBUTTON)
		self.remove_widget(LISTVIEW)

		updateList = self.ListFiles()
		list_adapter = ListAdapter(data=["{}".format(i) for i in updateList], cls=ListItemButton, sortedKeys=[])
		LISTVIEW = ListView(adapter=list_adapter)
		self.add_widget(LISTVIEW)
		self.ReAddButtons()


	def OnSwitch(self):
		#TODO: Add more method needed on screen switch 
		self.SetClientList() 
		
	def SetClientList(self):
		pass

	#TODO: Implement screen design
 	def __init__(self, **kwargs):
		global LISTVIEW
		global UPLOADBUTTON
		global DOWNLOADBUTTON

		super(TransferScreen, self).__init__(**kwargs) 
		
		self.cols = 2 
		self.label = Label(size_hint_y=None, height=50) 
		self.add_widget(self.label) 
		
		self.listButton = Button(text='List Files', on_press=self.UpdateFtpDirectoryListing, size_hint_y=None, height = 50)
		self.add_widget(self.listButton) 
 
		self.fileChooser = FileChooserIconView(path="C:\\Users\\IEUser\\Desktop\\") 
		self.add_widget(self.fileChooser)

		updateList = self.ListFiles()
		list_adapter = ListAdapter(data=["{}".format(i) for i in updateList], cls=ListItemButton, sortedKeys=[])
		LISTVIEW = ListView(adapter=list_adapter)

		self.UpdateFtpDirectoryListing()

