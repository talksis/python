import RPi.GPIO as GPIO
import dht11
import time
import datetime
from tkinter  import *
import threading

root = Tk()

root.title="Test DHT11 Sensor"
lbl_time1=Label(root,text="현재시간", width=10)
lbl_time1.grid(row=0,column=1)
lbl_time2=Label(root,text="현재시간", width=30)
lbl_time2.grid(row=0,column=2)
lbl = Label(root, text="온도",width=10)
lbl.grid(row=1,column=1)
lbl_temp = Label(root, text="",width=30)
lbl_temp.grid(row=1,column=2)
lbl_temp['text']="Unknown"
lbl_time2['text']=str(datetime.datetime.now())
lbl_hu1=Label(root,text="습도",width=10)
lbl_hu1.grid(row=2,column=1)

lbl_hu2=Label(root,text="Unknown",width=30)
lbl_hu2.grid(row=2,column=2)
             
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)
def get_temp():
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            lbl_temp['text']=str(result.temperature)+"C"
            lbl_time2['text']=str(datetime.datetime.now())
            lbl_hu2['text']=str(result.humidity)
        time.sleep(1)
    return (str(datetime.datetime.now()), result.temperature,result.humidity)
th = threading.Thread(target=get_temp)
th.daemon=True
th.start()
root.mainloop()
