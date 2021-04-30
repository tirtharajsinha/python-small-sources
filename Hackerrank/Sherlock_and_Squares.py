

import math
def squares(a, b):
    count=0
    c=int(math.sqrt(a))
    d=int(math.sqrt(b))
    for i in range(c,d+1):
        val=i*i
        if val>=a and val<=b:
            count+=1
    return count

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        a,b=[int(x)for x in input().split()]
        print(squares(a,b))
