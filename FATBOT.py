import webbrowser
import time
import os

print '\t\t\t ######################################'
print '\t\t\t ##                                  ##'
print '\t\t\t ##   Author : Tn-Sec (riadh selmi   ##'
print '\t\t\t ######################################'




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
