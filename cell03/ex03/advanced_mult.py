#!/usr/bin/env python3
import sys
z = sys.argv
if len(z) > 1 :
    print("none")
    sys.exit(0)
x = 0
while x <= 10 :
    print(f"Table de {x}: ", end="")
    y = 0
    while y <= 10 :
        print(f"{x * y} ", end="")
        y += 1
    print()
    x += 1