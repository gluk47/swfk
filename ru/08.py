#!/usr/bin/env python3

import turtle
import sys

t = turtle.Pen()
for x in range(1,9):
    t.forward(100)
    t.left(225)
sys.stdin.readline()

t.reset()
for x in range(1,38):
    t.forward(100)
    t.left(175)
sys.stdin.readline()

t.reset()
for x in range(1,20):
    t.forward(100)
    t.left(95)
sys.stdin.readline()

t.reset()
for x in range(1,19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
sys.stdin.readline()
