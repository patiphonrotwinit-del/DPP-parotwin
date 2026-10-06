#!/usr/bin/env python3
import sys

x = sys.argv[1:]

if len(x) < 2:
    print("None")
else :
    re_x = x[::-1]
    for rs in re_x :
        print(rs)
