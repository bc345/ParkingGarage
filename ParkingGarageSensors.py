#Libraries
import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
#set GPIO Pins
PIN_TRIGGER1 = 18
PIN_ECHO1 = 23

PIN_TRIGGER2 = 25
PIN_ECHO2 = 24

PIN_TRIGGER3 = 6
PIN_ECHO3 = 5

GPIO.setwarnings(False)
#set GPIO direction (IN / OUT)
GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
GPIO.setup(PIN_ECHO1, GPIO.IN)

GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
GPIO.setup(PIN_ECHO2, GPIO.IN)

GPIO.setup(PIN_TRIGGER3, GPIO.OUT)
GPIO.setup(PIN_ECHO3, GPIO.IN)

while True:
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
    print ("Sensor 1 Distance:", distance, "cm")
    time.sleep(1)
    
    if (distance <= 183):
        print("Parking spot is taken \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        print("Parking spot is empty \n")
        time.sleep(0.01)
        
    
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
    print ("Sensor 2 Distance:", distance, "cm")
    time.sleep(1)
    
    if (distance <= 183):
        print("Parking spot is taken \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        print("Parking spot is empty \n")
        time.sleep(0.01)
    
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

    if (distance <= 183):
        print("Parking spot is taken \n")                                                                                                                                                                           
        time.sleep(0.01)
    elif (distance > 183):
        print("Parking spot is empty \n")
        time.sleep(0.01)
