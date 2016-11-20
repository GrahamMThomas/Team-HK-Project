from ftplib import FTP, error_perm 
from kivy.uix.popup import Popup
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionPrevious
from kivy.uix.actionbar import ActionButton
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import sys
import io

def closePopup(self):
	listingErrorPopup.dismiss()

errorListingMessage = Label(text = "")
listingBoxLayout = BoxLayout(orientation = 'vertical')
listingBoxLayout.add_widget(errorListingMessage)
listingBoxLayout.add_widget(Button(text = "OK", size_hint_y = .4, on_release = closePopup))
listingErrorPopup = Popup(title = "Error: Listing", content = listingBoxLayout, size_hint = (.5,.4))

class FTPConnectionService: 
	ftp = FTP() 
	ftpDirectory = '/'

	@classmethod 
	def ConnectToFtpServer(self, host, port, username, password): 
		try: 
			self.ftp.connect(host, int(port)) 
			messageReceivedForLoginInformation = self.ftp.login(username, password) 
			print "FTP login received: {}".format(messageReceivedForLoginInformation) 
			return True 
		except Exception, e: 
			print "[ERROR] FTP connection failed with error: {}".format(e) 
			return False 
			
	@classmethod
	def FtpBackCommand(self, directory):
		ls = []
		self.ftpDirectory = directory
		lengthOfDirectory = len(directory)
		if(lengthOfDirectory > 1):
			secondLast = directory[-2]
			Last = directory[-1]
			checkingForBack = secondLast + Last
			if checkingForBack == '//':
				self.ftp.retrlines('LIST %s' % self.ftpDirectory, ls.append)
		
		else:
			self.ftp.retrlines('LIST %s' % self.ftpDirectory, ls.append)
		
		return self.ListParser(ls)
						
	@classmethod 
	def FtpListCommand(self, directory = '/'):
		ls = []
		if directory[-1] == '/':
			try:
				self.ftpDirectory += directory
				self.ftpDirectory.replace('//','/')
				print "Directory: {}".format(self.ftpDirectory)
				self.ftp.retrlines('LIST %s' % self.ftpDirectory, ls.append)
			except error_perm, msg:
				errorListingMessage.text = ""
				parsedErrorMessage = (str(msg)).split(" ")[1:]
				for item in parsedErrorMessage:
					errorListingMessage.text = errorListingMessage.text + str(item) + " "	
				listingErrorPopup.open()
		else:
			self.ftp.retrlines('LIST', ls.append)

		return self.ListParser(ls)

	@classmethod
	def ListParser(self, ls):
		files = []
		print ls
		for iteratorInFileListing in ls:
			fileProperties = iteratorInFileListing.split()
			if fileProperties[2] == '<DIR>' or fileProperties[0][0] == 'd':
				files.append("%s/" % fileProperties[-1])
			else:
				files.append(fileProperties[-1])
			print(iteratorInFileListing)
		home_keyword = '..'
		files.insert(0,home_keyword)
		return files

	@classmethod
	def Download(self, filename, destinationDir):
		if destinationDir[-1] != '\\':
			destinationDir += '\\'
		print "Downloading {0} to {1}{0}".format(filename.split('/')[-1],destinationDir)
		try:
			return self.ftp.retrbinary('RETR %s' % filename, open('{1}{0}'.format(filename.split('/')[-1], destinationDir), 'wb').write)
		except IOError as err:
			return err
		
	@classmethod
	def Upload(self, filename, destinationDir):
		fileToUpload = filename.split('\\')[-1]
		print ("Uploading %s to %s")%(filename, destinationDir)
		print ("Destination Directory = {}{}").format(destinationDir,fileToUpload)
		f = open(filename, 'rb')
		uploadCommandOutput = self.ftp.storbinary('STOR {}{}'.format(destinationDir, fileToUpload), f)
		f.close()	
		return uploadCommandOutput
	
	@classmethod
	def thisRemove(self, filename):
		try:
			self.ftp.delete(filename)
			return True
		except Exception as ex:
			print("Error: %s")%(ex)
			return False
				
	@classmethod
	def thisUpload(self, filename, destinationDir):
		bio = io.BytesIO('')
		uploadCommandOutput = self.ftp.storbinary('STOR {}{}'.format(destinationDir, filename), bio)
		return uploadCommandOutput
	
	@classmethod
	def renameFile(self, currentFileName, newFileName):
		try:
			self.ftp.rename(currentFileName, newFileName)
			return True
		except Exception as ex:
			print("Error: ", ex)
			return False
				
	@classmethod
	def GetCurrentDirectory(self):
		return self.ftpDirectory

def __init__(self): 
	pass 