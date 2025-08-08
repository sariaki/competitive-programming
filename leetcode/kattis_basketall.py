#! /usr/bin/python3
import sys
 
for line in sys.stdin:
    line = str(line)
    alice = 0
    barbara = 0

    for i in range(1, len(line), 2):
        person = line[i-1]
        if person == 'A':
            alice += int(line[i])
        elif person == 'B':
            barbara += int(line[i])

    if alice > barbara:
        print("A")
    else:
        print("B")