n, m, q = map(int, input().split())

col = []
mp = {}

for item in input().split():
    col.append(item)
    mp[item] = [-float('inf'), float('inf')]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
for _ in range(q):
    c, a, b = input().split()
    b = int(b)
    if a == '>':
        mp[c][0] = max(mp[c][0], b)
    else:
        mp[c][1] = min(mp[c][1], b)

excludedRows = set()

for i in range(m):
    for k in range(n):
        if mp[col[i]][0] >= arr[k][i] or arr[k][i] >= mp[col[i]][1]:
            excludedRows.add(k)

ans = 0

for i in range(n):
    if i not in excludedRows:
        for j in range(m):
            ans += arr[i][j]

print(ans)
