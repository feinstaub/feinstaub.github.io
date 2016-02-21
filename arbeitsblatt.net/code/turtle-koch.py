#!/usr/bin/python3
# -*- coding: utf-8 -*-

# requires python3-tk

from turtle import *
import time
import math

def koch(a, n):
    if n > 0:
        koch(a / 3.0, n - 1)
    else:
        forward(a)

    left(60)

    if n > 0:
        koch(a / 3.0, n - 1)
    else:
        forward(a)

    right(120)

    if n > 0:
        koch(a / 3.0, n - 1)
    else:
        forward(a)

    left(60)

    if n > 0:
        koch(a / 3.0, n - 1)
    else:
        forward(a)

speed(10)
setheading(0) # east
koch(300, 3)

time.sleep(1)
