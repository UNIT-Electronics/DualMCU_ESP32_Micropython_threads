"""
Unit Electronics 2023
ADC
Obtain the read on ADC Port from ESP32
"""
from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(15))

while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)