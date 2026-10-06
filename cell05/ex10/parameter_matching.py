#!/usr/bin/env python3
import sys
if len(sys.argv) != 2 :
    print("None")
    sys.exit(0)

x = sys.argv[1]
y = input("What was the parameter? ")

if y == x :
        print("Good Jop!!")
else :
        print("Nope, sorry...")

