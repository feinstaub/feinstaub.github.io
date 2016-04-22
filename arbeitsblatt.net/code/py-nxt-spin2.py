#!/usr/bin/env python

# copied from /home/gregor/dev/src/nxt-python-examples/spin.py

import nxt.locator
from nxt.motor import *

def spin_around(b):
    m_left = Motor(b, PORT_B)
    m_left.turn(100, 360)
    m_right = Motor(b, PORT_C)
    m_right.turn(-100, 360)

    #while True:
    m_left.turn(50, 360)
    m_left.turn(-50, 360)
    #m_left.turn(127, 360)
    m_left.turn(50, 360)

    x = 10
    flip = 1
    while True:
        m_left.turn(flip * 100, x)
        x = x + 10
        flip = -flip


b = nxt.locator.find_one_brick()
spin_around(b)

