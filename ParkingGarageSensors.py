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
#Trigger and Echo for Sensor 1
PIN_TRIGGER1 = 18
PIN_ECHO1 = 23
#Trigger and Echo for Sensor 2
PIN_TRIGGER2 = 25
PIN_ECHO2 = 24
#Trigger and Echo for Sensor 3
PIN_TRIGGER3 = 6
PIN_ECHO3 = 5

i=0
GPIO.setwarnings(False)
#set GPIO direction (IN / OUT)
GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
GPIO.setup(PIN_ECHO1, GPIO.IN)

GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
GPIO.setup(PIN_ECHO2, GPIO.IN)

GPIO.setup(PIN_TRIGGER3, GPIO.OUT)
GPIO.setup(PIN_ECHO3, GPIO.IN)


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
    printThis = "\n"+"Sensor 1 Distance in cm is: "+str(distance)
    print (printThis)
    time.sleep(1)
    
    if (distance <= 183):
        #print("Sensor 1 Parking spot is full \n")
        distanceChecker[0] = 0                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        #print("Sensor 1 Parking spot is available \n")
        distanceChecker[0] = 1
        time.sleep(0.01)
    
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
    #Floor1[1] = distance
    printThis = "\n"+"Sensor 2 Distance in cm is: "+str(distance)
    print (printThis)
    time.sleep(1)
    
    if (distance <= 183):
        #print("Sensor 2 Parking spot is full \n")
        distanceChecker[1] = 0                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        #print("Sensor 2 Parking spot is available \n")
        distanceChecker[1] = 3
        time.sleep(0.01)
    #distanceChecker[1]=distance
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
    printThis = "\n"+"Sensor 3 Distance in cm is: "+str(distance)
    print (printThis)
    time.sleep(1)
    #distanceChecker[2]=distance

    if (distance <= 183):
        #print("Sensor 3 Parking spot is full \n")
        distanceChecker[2] = 0                                                                                                                                                                            
        time.sleep(0.01)
    elif (distance > 183):
        #print("Sensor 3 Parking spot is available \n")
        distanceChecker[2] = 2
        time.sleep(0.01)
        
    #print(distanceChecker[2])

    

    
def refreshThread():
    d1 = threading.Thread(target=distanceSensor_1, args=())
    d2 = threading.Thread(target=distanceSensor_2, args=())
    d3 = threading.Thread(target=distanceSensor_3, args=())


    d1.start()
    d2.start()
    d3.start()
    d1.join()
    d2.join()
    d3.join()
    
firstFloorFile = "/home/pi/projects/f0.txt"

while True:
    d = threading.Thread(target=refreshThread, args=())
    d.start()
    d.join()

    with open(firstFloorFile, 'w') as file:
        print(str(distanceChecker[0])+" "+str(distanceChecker[1])+" "+str(distanceChecker[2])+" "+str(distanceChecker[3])+" "+"0"+" "+"0"+" "+"0"+" "+"0")
        file.write(str(distanceChecker[0])+" "+str(distanceChecker[1])+" "+str(distanceChecker[2])+" "+str(distanceChecker[3])+" "+"0"+" "+"0"+" "+"0"+" "+"0")
        file.flush()


    time.sleep(0.1)



