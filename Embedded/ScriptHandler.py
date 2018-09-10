import sys
import subprocess
import urllib.request


def testingMenu():
	print ("usage: ")
	print ("-read [scriptPath arguments]")

#Create a data structure with list of scripts and their location and parameters
def handleScript(executor, path, argument):
	try:
		process = subprocess.Popen([executor, path, argument], stdout=subprocess.PIPE, shell=True)
		(out, err) = process.communicate()
		print ("script output:", out)
		#getToken()
	except Exception as e:
		print(str(e))

def getToken():
	#needs to be reworked
	try:
		contents = urllib.request.urlopen('192.168.0.101:8000/api/auth/token/username=virtue&password=virtuevirtue')
		print(contents)
	except Exception as e:
		print(str(e))

def selectAction(): #based on the handled request select action to be taken

def main():
	executor = "python"
	argsIndex = -1
	global path      # = "C:/Users/Elvir/Desktop/testVenus.py"
	global argument  #= "-hello" #or -bye
	
	testingMenu()

	try:
		argsIndex = sys.argv.index("-read")
		path      = sys.argv[argsIndex + 1]
		argument  = sys.argv[argsIndex + 2]

		handleScript(executor, path, argument)
	except Exception as e:
		print(str(e))

	print("Nothing Happend before this ??? ")
	sys.exit(1)

main()
