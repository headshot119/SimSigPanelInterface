import sys
import socket
import time
import Interface_Gateway_Input_Connection
import RPi.GPIO as GPIO

def main():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Call point normal
        GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Call point Reverse

	s, onConnectMessage = Interface_Gateway_Input_Connection.connect('127.0.0.1', 50505, 'PIPI', 'anytown', '0.0.3', '4.5.8.0')

	pointStatus = 0 # 0 is center, 1 is N, 2 is R
	Input = 0

	while 1:

		#Read pins 5 + 6

		if (GPIO.input(5) == 0): # As in switch is at 5
			#Key Normal
			Input = 1
			print("1")
		elif (GPIO.input(6) == 0): # As in switch is at 6
			Input = 2
			print("2")
		elif (GPIO.input(5) == 1 and GPIO.input(6) == 1):
                        print("0")
                        Input = 0
		else:
                        print("Oh dear")
			

		if (Input == 0 and pointStatus != 0): #The point needs to be center but isn't
			if (pointStatus == 1):
				pointStatus = 0
				#Send a key normal packet
				s.send("PB0000|")
			else:
				pointStatus = 0
				#Send a key reverse packet
				s.send("PC0000|")
		elif (Input == 1 and pointStatus != 1): #The point needs to be keyed normal but isn't
			if (pointStatus == 0):
				pointStatus = 1
				#Send a key normal packet
				s.send("PB0000|")
			else:
				pointStatus = 1
				#Send a key Normal packet
				#Send a key Normal packet
				s.send("PB0000|")
				s.send("PB0000|")
		elif (Input == 2 and pointStatus != 2): #The point needs to be keyed reverse but isn't	
			if (pointStatus == 0):
				pointStatus = 2
				#Send a key reverse packet
				s.send("PC0000|")
			else:
				pointStatus = 2
				#Send a key reverse packet
				#Send a key reverse packet	
				s.send("PC0000|")
				s.send("PC0000|")

if __name__ == "__main__":
	main()
