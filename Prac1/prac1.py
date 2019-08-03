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
