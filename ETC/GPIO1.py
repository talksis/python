import RPi.GPIO as GPIO
import time

ledPin =7
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(ledPin,GPIO.IN)
prev_push =time.clock()
last_btn_state = 0
current_btn_state=0
pin_state=0
while True:
    i =GPIO.input(ledPin)
    if last_btn_state!=i:
        print("change")
    last_btn_state=i
    
    
        
    
    

