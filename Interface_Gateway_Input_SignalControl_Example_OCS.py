import sys
import socket
import time
import RPi.GPIO as GPIO
 
 
def main():
 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
    s, onConnectMessage = Interface_Gateway_Input_Connection.connect('127.0.0.1', 50505, 'PIPI', 'anytown', '0.0.3', '4.5.8.0')

    entranceState527 = 0
    route527BMState = 0
         
    while True:
 
        entranceS527 = GPIO.input(18)
        exitS527 = GPIO.input(23)
        if (entranceS527 == 0): # Entrance Switch is turned on
            if (route527BMState == 0): #Route isn't set
                #Set the route
                commandToSend = "SA" +  signalDict['S527'] +  signalDict['S529'] + "00" + signalDict['S527'] + "----|"
                s.send(commandToSend)
                print ("Route set R527BM")
                route527BMState = 1                               
        else: #Entrance Switch is turned off
            if (route527BMState == 1 and entranceS527 == 1): #If the route is set
                #Cancel the Route
                commandToSend = "zD" +  signalDict['S527'] + "|"
                s.send(commandToSend)
                print ("Route Cancelled R527BM")
                route527BMState = 0
                 
 
    s.close()
 
if __name__ == "__main__":
    main()
