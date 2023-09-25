"""
Unit Electronics 2023
        >o)
        (_>   
file: multicore.py
author: Cesar
version: 0.0.2
revision: 0.0.1
context: Multicore example semaphore 

"""
import machine
import utime
import _thread
led1 = machine.Pin(25, machine.Pin.OUT)
led2 = machine.Pin(26, machine.Pin.OUT)

sLock = _thread.allocate_lock()

def toggle_led():
    led1.value(not led1.value())

def CoreTask():
    while True:
        sLock.acquire()
        print("Entered into the second Thred")
        utime.sleep(1)
        led2.on()  
        print("Led 2 turned on")
        utime.sleep(2)
        led2.off() 
        print("Led 2 turned off")
        utime.sleep(1)
        print("Exiting from the 2nd Thread")
        utime.sleep(1)
        sLock.release()
_thread.start_new_thread(CoreTask, ())
while True:
    # We acquire the semaphore lock
    sLock.acquire()
    print("Entered into the main Thred")
    toggle_led()
    utime.sleep(0.15)
    print("Led 1 started to toggle.")
    utime.sleep(1)
    print("Exiting from the main Thread")
    utime.sleep(1)
    # We release the semaphore lock
    sLock.release()