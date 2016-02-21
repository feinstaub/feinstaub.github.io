#!/usr/bin/python3
# -*- coding: utf-8 -*-

# requires python3-tk

from turtle import *
import time
import math

a = 100
left(90)
forward(a)
right(45)
forward(math.sqrt(2) * a / 2)
right(90)
forward(math.sqrt(2) * a / 2)
right(135)
forward(a)
left(135)
forward(math.sqrt(2) * a)
left(135)
forward(a)
left(135)
forward(math.sqrt(2) * a)
left(135)
forward(a)

time.sleep(1)
