from itertools import combinations

n=int(input())
arr=[x for x in input().split()]
c=int(input())
com=list(combinations(arr,c))
count=0
for c in com:
    if "a" in c:
        count+=1

print(count/len(com))
