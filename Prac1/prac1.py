#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <BERTHA NAFUNU>
Student Number: <MFNBER001>
Prac: <Prac 1>
Date: <29/07/2019>
"""

import RPi.GPIO as GPIO  #importing GPIO pins

from time import sleep   # importing  the sleep time command

GPIO.setmode(GPIO.BOARD) #importing itertools

List1 = [29, 31] #list of inputs that is the button1 and 2

List2 = [11, 13, 15]    #list of the outputs that is the leds 1,2 and 3

listflow =list(product([0,1], repeat=3)) #outputs of the 3 bit counter


def main():
	print("Executing Program")
	
	counter = 0 #simple counter variable to remember progression in bit counter 
	
	sleep(1)  #setting sleeping time to 1second
	
	button1 = GPIO.gpio_function(31)  #initialising port 31 for button1
	
	print(button1)
	
	button2 = GPIO.gpio_function(33)  #initialising port 33 for button 2
	
	print(button2)
	
	while(True):
		
		print("while loop is working")
		
		#function to make the LEDs increase by one when a button is pressed
		
		#make Leds increase from 0 to 1 if button1 is pressed
		if GPIO.event_detected(29):#for button1
			
			counter= counter + 1
                        
			if counter ==8:
				
				counter=0

			print(sequenceList[counter])
			
			GPIO.output(List2, sequenceList[counter])
			
			sleep(.1)  #sleep for 0.1 seconds

			print("button1 works")	
			
			#make LEDs decrease by 1 with SW2 press
			if GPIO.event_detected(31):
				
				counter-=1
				
				if counter ==-1:
					
					counter=7
	
				print(sequenceList[counter])
				
				GPIO.output(List2, sequenceList[counter])
				
				sleep(.3) #sleep for 0.3s
	
				print("button2 works")
	
			sleep(1) #sleep for 1s
			

if __name__ == "__main__":
	
	try:  
		
		GPIO.setmode(GPIO.BOARD)  #initialising main loop so it does not iterate
		
		
		GPIO.setup(List2, GPIO.OUT, initial=GPIO.LOW)   #GPIO set to output
		
		
		GPIO.setup(List1, GPIO.IN) #GPIO set to input
		
		
		GPIO.setup(List1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		
		#add edge detection and debouncing, out of loop to avoid error 
		GPIO.add_event_detect(29, GPIO.RISING, bouncetime=200)#applying edge of detection on button1
		
		
		GPIO.add_event_detect(31, GPIO.RISING, bouncetime=200)#applying edge of detection on button2	
		
    
		while True:
			
			
			main()		
			
			
				
	except KeyboardInterrupt:  
		
		print("Exiting gracefully")
		
		
		GPIO.cleanup()      #turning off the GPIO	
		
	except Exception as e:
		
		GPIO.cleanup()
		
		print("an error occured")
		
		print(e.message)	
		