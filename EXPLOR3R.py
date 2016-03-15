#!/usr/bin/python

from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from DiffRobot import *

class EXPLOR3R(DiffRobot):
    """docstring for EXPLOR3R"""
    def __init__(
        self, diam=5.5, width=14, r_address=OUTPUT_A, l_address=OUTPUT_B,
        us_address=INPUT_4, ts_address=None, cs_address=None):
    
        DiffRobot.__init__(self, diam, width)
        
        self.us = UltrasonicSensor(us_address)
        if ts_address != None:
            self.ts = TouchSensor(ts_address)
        if cs_address != None:
            self.cd = ColorSensor(cs_address)
