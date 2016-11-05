from kivy.uix.gridlayout import GridLayout 
from kivy.uix.screenmanager import Screen 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.uix.label import Label 
from kivy.adapters.dictadapter import ListAdapter 
from kivy.uix.listview import ListView, ListItemButton 
from kivy.uix.boxlayout import BoxLayout

from Settings import * 
from HKftp import * 
from kivy.uix.button import Button 
import os

selected_value_client_side = None

def pressed(self,instance,cls):
	print(selected_value_client_side)

currentDirectory = os.getcwd()
# FIXME: All the global need to go away.
UPLOADBUTTON = Button()
DOWNLOADBUTTON = Button()
LISTVIEW = ListView()
LISTADAPTER = ListAdapter(data=[], cls=ListItemButton, sortedKeys=[])
FILECHOOSER = FileChooserIconView(path=currentDirectory, multiselect = True, on_submit = pressed)

def closeDownloadPopup(self):
	popupErrorMessage.dismiss()

def openPopup(msg):
	errorLabelMessage.text = str(msg)
	popupErrorMessage.open()
	
errorTransferBoxLayout = BoxLayout(orientation = 'vertical')
errorLabelMessage = Label(text = "No File selected", font_size = 18)
errorTransferBoxLayout.add_widget(errorLabelMessage)
confirmationError = Button(text = "OK", size_hint_y = .4, on_release = closeDownloadPopup)
errorTransferBoxLayout.add_widget(confirmationError)
popupErrorMessage = Popup(title = "Error: Transfer Status", content = errorTransferBoxLayout, size_hint = (.5,.4))


class TransferScreen(GridLayout, Screen):

	def DownloadFile(self, instance = None):
		if LISTADAPTER.selection:
			filename =  FTPConnectionService.GetCurrentDirectory() + (str(LISTADAPTER.selection[0]).split('=')[1])[0:-1]
			openPopup(FTPConnectionService.Download(filename,FILECHOOSER.path))
				
		else:
			openPopup("No File Selected")
			print "Error: No file selected FROM DOWNLOAD SIDE"
	
	def UploadFile(self, instance = None):
		selected_value_client_side = FILECHOOSER.selection
		uploadFileName = None
		
		for item in selected_value_client_side:
			uploadFileName = item
						
		if selected_value_client_side:
			FTPConnectionService.Upload(uploadFileName, FTPConnectionService.GetCurrentDirectory())
		else:
			popupErrorMessageDownload.open()
			print("Error: No file selected FROM UPLOAD SIDE")
	
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

		UPLOADBUTTON = Button(text='UPLOAD', size_hint_y=None, height=50, on_press = self.UploadFile)
		self.add_widget(UPLOADBUTTON)

		DOWNLOADBUTTON = Button(text='DOWNLOAD', on_press=self.DownloadFile, size_hint_y=None, height=50)
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
		
	