from ftplib import FTP 
from kivy.core.window import Window 


#TODO: Determine if this is the best way to deal with persistent ftp objects 


class FTPConnectionService: 
	ftp = FTP() 
	
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
		self.ftp.retrlines('LIST %s' % directory, ls.append)
		return self.ListParser(ls)

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

	#TODO: Add more methods here!

def __init__(self): 
	pass 
