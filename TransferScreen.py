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
LISTADAPTER = ListAdapter(data=[], cls=ListItemButton, sortedKeys=[])
FILECHOOSER = FileChooserIconView(path="C:\\Users\\IEUser\\Desktop\\")

class TransferScreen(GridLayout, Screen):

	def DownloadFile(self, instance = None):
		if LISTADAPTER.selection:
			filename =  FTPConnectionService.GetCurrentDirectory() + (str(LISTADAPTER.selection[0]).split('=')[1])[0:-1]
			FTPConnectionService.Download(filename,FILECHOOSER.path)
		else:
			print "Error: No file selected"


	#-------------------------------------------FTP DIRECTORY----------------------------------
	def ListFiles(self, directory = '/', instance = None):
		#TODO: Add formatting here
		if LISTADAPTER.selection:
			output = FTPConnectionService.FtpListCommand((str(LISTADAPTER.selection).split('=')[1])[0:-2])
		else:
			output = FTPConnectionService.FtpListCommand(directory)
		return output

	def ReAddButtons(self,instance = None):
		global UPLOADBUTTON
		global DOWNLOADBUTTON

		UPLOADBUTTON = Button(text='>>>>', on_press=self.ListFiles, size_hint_y=None, height=50)
		self.add_widget(UPLOADBUTTON)

		DOWNLOADBUTTON = Button(text='<<<<', on_press=self.DownloadFile, size_hint_y=None, height=50)
		self.add_widget(DOWNLOADBUTTON)

	def UpdateFtpDirectoryListing(self, instance = None):
		global LISTVIEW
		global UPLOADBUTTON
		global DOWNLOADBUTTON
		global LISTADAPTER
		# Removing old widgets
		self.remove_widget(UPLOADBUTTON)
		self.remove_widget(DOWNLOADBUTTON)
		self.remove_widget(LISTVIEW)

		updateList = self.ListFiles()
		LISTADAPTER = ListAdapter(data=["{}".format(i) for i in updateList], cls=ListItemButton, sortedKeys=[])
		LISTVIEW = ListView(adapter=LISTADAPTER)
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
		global LISTADAPTER

		super(TransferScreen, self).__init__(**kwargs) 
		
		self.cols = 2 
		self.label = Label(size_hint_y=None, height=50) 
		self.add_widget(self.label) 
		
		self.listButton = Button(text='List Files', on_press=self.UpdateFtpDirectoryListing, size_hint_y=None, height = 50)
		self.add_widget(self.listButton) 

		self.add_widget(FILECHOOSER)

		updateList = self.ListFiles()
		LISTADAPTER = ListAdapter(data=["{}".format(i) for i in updateList], cls=ListItemButton, sortedKeys=[])
		LISTVIEW = ListView(adapter=LISTADAPTER)

		self.UpdateFtpDirectoryListing()

