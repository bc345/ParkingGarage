import numpy as np
import array as arr
import random as random
import string 
Floor1=np.empty([10])
distanceChecker=([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#Libraries
import RPi.GPIO as GPIO
import time
import threading
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
PIN_TRIGGER4 = 17
PIN_ECHO4 = 27
#Trigger and Echo for Sensor 4
PIN_TRIGGER5 = 13
PIN_ECHO5 = 26
#Trigger and Echo for Sensor 5
PIN_TRIGGER6 = 12
PIN_ECHO6 = 16
#Trigger and Echo for Sensor 6
i=0
GPIO.setwarnings(False)
#set GPIO direction (IN / OUT)
GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
GPIO.setup(PIN_ECHO1, GPIO.IN)

GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
GPIO.setup(PIN_ECHO2, GPIO.IN)

GPIO.setup(PIN_TRIGGER3, GPIO.OUT)
GPIO.setup(PIN_ECHO3, GPIO.IN)

GPIO.setup(PIN_TRIGGER4, GPIO.OUT)
GPIO.setup(PIN_ECHO4, GPIO.IN)

GPIO.setup(PIN_TRIGGER5, GPIO.OUT)
GPIO.setup(PIN_ECHO5, GPIO.IN)

GPIO.setup(PIN_TRIGGER6, GPIO.OUT)
GPIO.setup(PIN_ECHO6, GPIO.IN)

def distanceSensor_1():
    #Sensor 1:
    GPIO.output(PIN_TRIGGER1, GPIO.LOW)
    #print ("Waiting for sensor 1 to settle")
    time.sleep(2)
    #print("Calculating sensor 1 distance")
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
    printThis = "Sensor 1 Distance in cm is: "+str(distance)
    print (printThis)
    time.sleep(1)
    
    if (distance <= 183):
        #print("Sensor 1 Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        #print("Sensor 1 Parking spot is available \n")
        time.sleep(0.01)
    distanceChecker[2]=distance
    #These if statements determine the range, value of 183 is used because approx 183cm is in 6ft.

def distanceSensor_2():
    #Sensor 2:
    GPIO.output(PIN_TRIGGER2, GPIO.LOW)
    #print ("Waiting for sensor 2 to settle")
    time.sleep(2)
    #print("Calculating sensor 2 distance")
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
    printThis = "Sensor 2 Distance in cm is: "+str(distance)
    print (printThis)
    time.sleep(1)
    
    if (distance <= 183):
        #print("Sensor 2 Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        #print("Sensor 2 Parking spot is available \n")
        time.sleep(0.01)
    distanceChecker[1]=distance
    #print( distanceChecker[1]) 

def distanceSensor_3():
    #Sensor 3:
    GPIO.output(PIN_TRIGGER3, GPIO.LOW)
    #print ("Waiting for sensor 3 to settle")
    time.sleep(2)
    #print("Calculating sensor 3 distance")
    GPIO.output(PIN_TRIGGER3, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER3,GPIO.LOW)
    while GPIO.input(PIN_ECHO3) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO3) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    printThis = "Sensor 3 Distance in cm is: "+str(distance)
    print (printThis)
    time.sleep(1)
    distanceChecker[1]=distance

    if (distance <= 183):
        #print("Sensor 3 Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        #print("Sensor 3 Parking spot is available \n")
        time.sleep(0.01)
        
    #print(distanceChecker[2])

    
def distanceSensor_4():
    GPIO.output(PIN_TRIGGER4, GPIO.LOW)
    print ("Waiting for sensor 4 to settle")
    time.sleep(2)
    print("Calculating sensor 4 distance")
    GPIO.output(PIN_TRIGGER4, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER4,GPIO.LOW)
    while GPIO.input(PIN_ECHO4) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO4) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    #Floor1[0] = distance
    printThis = "Sensor 3 Distance in cm is: "+str(distance)
    print (printThis) 
    time.sleep(1)
    
    if (distance <= 5):
        print("Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 5):
        print("Parking spot is available \n")
        time.sleep(0.01)
    distanceChecker[0]=distance
    
def distanceSensor_5():
    GPIO.output(PIN_TRIGGER5, GPIO.LOW)
    print ("Waiting for sensor 5 to settle")
    time.sleep(2)
    print("Calculating sensor 5 distance")
    GPIO.output(PIN_TRIGGER5, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER5,GPIO.LOW)
    while GPIO.input(PIN_ECHO5) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO5) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    #Floor1[0] = distance
    printThis = "Sensor 3 Distance in cm is: "+str(distance)
    print (printThis) 
    time.sleep(1)
    
    if (distance <= 5):
        print("Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 5):
        print("Parking spot is available \n")
        time.sleep(0.01)
    distanceChecker[2]=distance

def distanceSensor_6():
    GPIO.output(PIN_TRIGGER6, GPIO.LOW)
    print ("Waiting for sensor 6 to settle")
    time.sleep(2)
    print("Calculating sensor 6 distance")
    GPIO.output(PIN_TRIGGER6, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER6,GPIO.LOW)
    while GPIO.input(PIN_ECHO6) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO6) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    #Floor1[0] = distance
    printThis = "Sensor 3 Distance in cm is: "+str(distance)
    print (printThis) 
    time.sleep(1)
    
    if (distance <= 5):
        print("Parking spot is full \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 5):
        print("Parking spot is available \n")
        time.sleep(0.01)
    distanceChecker[0]=distance
    
def refreshThread():
    d1 = threading.Thread(target=distanceSensor_1, args=())
    d2 = threading.Thread(target=distanceSensor_2, args=())
    d3 = threading.Thread(target=distanceSensor_3, args=())
    d4 = threading.Thread(target=distanceSensor_4, args=())
    d5 = threading.Thread(target=distanceSensor_5, args=())
    d6 = threading.Thread(target=distanceSensor_6, args=())

    d1.start()
    d2.start()
    d3.start()
    d4.start()
    d5.start()
    d6.start()
    
    i=0
    while (i<=9):
        
        distanceChecker[i];
        if distanceChecker[i]>0 and distanceChecker[i]>5:
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
