from itertools import product

n, val = map(int, input().split())
n = [[int(x) for x in input().split()[1:]] for _ in range(n)]
# print(len(list(product(*n))))
results = (sum(i**2 for i in x) % val for x in product(*n))

print(max(results))
