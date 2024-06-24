#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

with open ("file.txt") as f:
    for i in f.readlines():
        sleep(random.random())
        sys.stdout.write(i)
        sys.stdout.flush()
