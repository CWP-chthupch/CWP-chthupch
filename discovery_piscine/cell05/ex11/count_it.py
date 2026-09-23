#!/usr/bin/env python3
import sys

params = sys.argv[1:]
if len(params) == 0:
    print("none")
else:
    print("parameters: " + str(len(params)))
    for p in params:
        print(p + ": " + str(len(p)))