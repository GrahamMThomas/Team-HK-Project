from ftplib import FTP 
from kivy.uix.popup import Popup
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionPrevious
from kivy.uix.actionbar import ActionButton

import sys

#TODO: Determine if this is the best way to deal with persistent ftp objects 

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
	def FtpListCommand(self, directory = '/'):
		ls = []
		if directory[-1] == '/':
			self.ftp.retrlines('LIST %s' % directory, ls.append)
			self.ftpDirectory = directory
		else:
			self.ftp.retrlines('LIST', ls.append)
			self.ftpDirectory = '/'
		return self.ListParser(ls)

	# TODO: Fix parser so works on all servers
	@classmethod
	def ListParser(self, ls):
		files = []
		for FileListing in ls:
			fileProperties = FileListing.split()
			if fileProperties[2] == '<DIR>':
				files.append("%s/" % fileProperties[3])
			else:
				files.append(fileProperties[3])
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
	def GetCurrentDirectory(self):
		return self.ftpDirectory

	#TODO: Add more methods here!

def __init__(self): 
	pass 
