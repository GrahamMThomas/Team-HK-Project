from ftplib import FTP
from kivy.core.window import Window

#TODO: Determine if this is the best way to deal with persistent ftp objects

class HKftp:
    ftp = FTP()

    @classmethod
    def HKConnect(cls, host, port, username, password):
        try:
            cls.ftp.connect(host, int(port))
            messageReceived = cls.ftp.login(username, password)
            print "FTP returned: {}".format(messageReceived)
            Window.size = (500, 500) #Change window size if connection successful
            return True
        except Exception, e:
            print "[ERROR] FTP connection failed with error: {}".format(e)
            return False

    @classmethod
    def HKList(cls, directory = '/'):
        output = cls.ftp.nlst(directory)
        return output

    #TODO: Add more methods here!

    def __init__(self):
        pass
