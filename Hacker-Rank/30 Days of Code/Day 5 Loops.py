#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n>=2 and n<=20:
        for i in range (10):
            print(str(n)+" x "+str(i+1)+" = "+str(n*(i+1)))