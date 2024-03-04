from collections import defaultdict

n, m, q = map(int, input().split())
A = defaultdict(int)

items = list(map(int, input().split()))
for a in items:
    A[a] += 1

items = list(map(int, input().split()))
for a in items:
    A[a] -= 1

ans = sum(abs(v) for v in A.values())

for _ in range(q):
    a, c, b = input().split()
    b = int(b)
    
    if a == '1':
        if c == 'A':
            if A[b] >= 0:
                ans += 1
            else:
                ans -= 1
            A[b] += 1
        else:
            if A[b] <= 0:
                ans += 1
            else:
                ans -= 1
            A[b] -= 1
    else:
        if c == 'A':
            if A[b] > 0:
                ans -= 1
            else:
                ans += 1
            A[b] -= 1
        else:
            if A[b] < 0:
                ans -= 1
            else:
                ans += 1
            A[b] += 1
        
    print(ans, end=' ')
