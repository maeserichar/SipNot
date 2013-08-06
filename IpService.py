import urllib2
import Config

def GetPublicIp():
	return urllib2.urlopen(Config.IpServiceUrl).read()

if __name__ == '__main__':
	print GetPublicIp()
