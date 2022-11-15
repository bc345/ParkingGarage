import numpy as np
import array as arr
import random as random
import string 
Floor1=np.empty([10])
distanceChecker=([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#Libraries
import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
#set GPIO Pins
PIN_TRIGGER1 = 18
PIN_ECHO1 = 23
#Trigger and Echo for Sensor 1
PIN_TRIGGER2 = 25
PIN_ECHO2 = 24
#Trigger and Echo for Sensor 2
PIN_TRIGGER3 = 6
PIN_ECHO3 = 5
#Trigger and Echo for Sensor 3
i=0
GPIO.setwarnings(False)
#set GPIO direction (IN / OUT)
GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
GPIO.setup(PIN_ECHO1, GPIO.IN)

GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
GPIO.setup(PIN_ECHO2, GPIO.IN)

GPIO.setup(PIN_TRIGGER3, GPIO.OUT)
GPIO.setup(PIN_ECHO3, GPIO.IN)

while True:
    #Sensor 1:
    GPIO.output(PIN_TRIGGER1, GPIO.LOW)
    print ("Waiting for sensor 1 to settle")
    time.sleep(2)
    print("Calculating sensor 1 distance")
    GPIO.output(PIN_TRIGGER1, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER1,GPIO.LOW)
    while GPIO.input(PIN_ECHO1) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO1) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    #commentFloor1[0] = distance
    print ("Sensor 1 Distance:", distance, "cm")
    time.sleep(1)
    
    if (distance <= 183):
        print("Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        print("Parking spot is available \n")
        time.sleep(0.01)
    distanceChecker[0]=distance
    #These if statements determine the range, value of 183 is used because approx 183cm is in 6ft.
    
    #Sensor 2:
    GPIO.output(PIN_TRIGGER2, GPIO.LOW)
    print ("Waiting for sensor 2 to settle")
    time.sleep(2)
    print("Calculating sensor 2 distance")
    GPIO.output(PIN_TRIGGER2, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER2,GPIO.LOW)
    while GPIO.input(PIN_ECHO2) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO2) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    Floor1[1] = distance
    print ("Sensor 2 Distance:", distance, "cm")
    time.sleep(1)
    
    if (distance <= 183):
        print("Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        print("Parking spot is available \n")
        time.sleep(0.01)
    distanceChecker[1]=distance
    print( distanceChecker[1])
    #Sensor 3:
    GPIO.output(PIN_TRIGGER3, GPIO.LOW)
    print ("Waiting for sensor 3 to settle")
    time.sleep(2)
    print("Calculating sensor 3 distance")
    GPIO.output(PIN_TRIGGER3, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER3,GPIO.LOW)
    while GPIO.input(PIN_ECHO3) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO3) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print ("Sensor 3 Distance:", distance, "cm")
    time.sleep(1)
    distanceChecker[2]=distance

    if (distance <= 183):
        print("Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        print("Parking spot is available \n")
        time.sleep(0.01)
        
    print(distanceChecker[1] )
    i=0


    while (i<=9):
        
        distanceChecker[i];
        if distanceChecker[i]>0 and distanceChecker[i]>183:
           Floor1[i]=int(1)
        else:
            Floor1[i]=int(0)
        if Floor1[1] == 1:
            Floor1[1] = int(2)
        if Floor1[2] == 1:
            Floor1[2] = int(3)
        print("wow")
        #else:
            #Floor1[i]=0
        print(Floor1[i])

        i=i+1
    a_file = open("f0.txt", "w")
    Filearray1=str(Floor1)
    a_file.write(Filearray1)
    a_file.close()
    a_file = open("f0.txt", "r")
    content = a_file.read()
    print(content)
    for ele in content:
        if ele in ".":
            content = content.replace(ele, "")
    for ele in content:
        if ele in "[":
            content = content.replace(ele, "")
    for ele in content:
        if ele in "]":
            content = content.replace(ele, "")
    print(content)
    a_file.close()
    a_file = open("f0.txt", "w")
    Filearray1=str(content)
    a_file.write(Filearray1)
    a_file.close()
