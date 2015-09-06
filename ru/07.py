#!/usr/bin/env python3

f=open('06.py')
g=open('/dev/null', 'w')
nlines=0
for line in f:
 nlines += 1

f=open('06.py')
for line in f:
 g.write(line)
 nlines -= 1
 print (nlines)

