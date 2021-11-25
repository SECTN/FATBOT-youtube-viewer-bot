import webbrowser
import time
import os




url = input("Enter YouTube URL : ")
refresh = input("Enter refresh rate(seconds) : ")
brow = input("Enter your default browser : ")

def OpenUrl():
	print("Successfully Viwed. ")
	os.system(" killall -9 " + brow)
	webbrowser.open(url)
	time.sleep(int(refresh))

for i in range(3):
	OpenUrl()
