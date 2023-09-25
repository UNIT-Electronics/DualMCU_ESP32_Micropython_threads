'''
Unit Electronics 2023
        >o)
        (_>
file: 2_blink.py
author: Cesar
version: 0.0.2
revision: 0.0.1
context: This code demonstrates a fundamental configuration of two LEDs within a loop thread using MicroPython.
'''
import machine
import _thread as threads
import time

led_pin = machine.Pin(25, machine.Pin.OUT)
led_pin2 = machine.Pin(26, machine.Pin.OUT)


def hilo_1():
     while True:
         
        led_pin.on()     
        time.sleep(1)  
        led_pin.off()   
        time.sleep(1)   


def hilo_2():
    while True:
        
        led_pin2.off() 
        time.sleep(1)
        led_pin2.on()
        time.sleep(1)  

threads.start_new_thread(hilo_1, ())
threads.start_new_thread(hilo_2, ())
