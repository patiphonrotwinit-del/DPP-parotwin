#!/usr/bin/env python3
x = [2, 8, 9, 48, 8, 22,-12, 2]
print(f"Original array: {list(x)}")
y = [item + 2 for item in x if (item + 2) >=5]
print(f"New array: {list(y)}")

