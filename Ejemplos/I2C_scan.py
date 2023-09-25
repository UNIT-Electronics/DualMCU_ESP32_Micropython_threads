"""
Unit Electronics 2023
        >o)
        (_>   
file: IC_scan.py
author: Cesar
version: 0.0.2
revision: 0.0.1
context: Scans for the I2C device address

"""

import machine
import binascii


i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))

devices = i2c.scan()
print("I2C Address: ", hex(devices[0]))