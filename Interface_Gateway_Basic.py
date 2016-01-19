import stomp
import time
import sys 

class MyListener(stomp.ConnectionListener): 
    def on_error(self, headers, message):  #What to do if an error is recieved
        print('Error Received %s' % message)
    def on_message(self, headers, message): #What to do if a message is recieved
        print (message)
    def on_disconnected(self): #What to do if the interface disconnects
    	print ("Interface Gateway Connection Lost")

dest='/topic/TD_ALL_SIG_AREA' #SimSig always uses this topic!
conn=stomp.Connection12([('127.0.0.1',51515)]) #Connect to the local server on the local port

conn.set_listener('test',MyListener()) 
conn.start() 
conn.send_frame('CONNECT',body='accept-version:1.1')
conn.subscribe(destination=dest, id=1, ack='auto')

while 1: #Infinite loop to keep the program alive
    time.sleep(0.01)

conn.disconnect() #Close the gateway