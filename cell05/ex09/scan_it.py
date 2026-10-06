#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3 :
    print("None")
    sys.exit(0)

x = sys.argv[1]
y = sys.argv[2]

xz = re.findall(re.escape(x),y)
count_y = len(xz)

if count_y == 0 :
    print("None")
else :
    print(count_y)
