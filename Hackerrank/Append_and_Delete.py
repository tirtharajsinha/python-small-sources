#!/bin/python3

import math
import os
import random
import re
import sys



def appendAndDelete(s, t, k):
    if t==s:
        if len(t)+len(s)<=k or (k)%2==0:
            return "yes"
        else:
            return "no"
    
    common=0
    for i in range(min(len(s),len(t))):
        if s[i]!=t[i]:
            break
        common+=1
        
    total=len(s)+len(t)-2*common
    
    if total==k or (total<k and (total-k)%2==0) or total+(2*common)<=k:
        return "yes"
    else:
        return "no"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)
    result=result.capitalize()
    fptr.write(result + '\n')

    fptr.close()
