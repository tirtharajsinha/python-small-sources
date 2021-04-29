#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    timeformat="%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, timeformat)
    t2 = datetime.strptime(t2, timeformat)
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
  t1 = "Sun 10 May 2015 13:54:36 -0700"
  t2 = "Sun 10 May 2015 13:54:36 -0000"

  delta = time_delta(t1, t2)
  print(delta)
        

    
# Input format
# t1,t2=Sun 10 May 2015 13:54:36 -0700,Sun 10 May 2015 13:54:36 -0000
