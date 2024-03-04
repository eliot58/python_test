def calculate_similarity(arr1, arr2):
    similarity = 0
    min_len = min(len(arr1), len(arr2))
    
    for i in range(min_len):
        if arr1[i] == arr2[i]:
            similarity += 1
        else:
            break
    
    return similarity

n = int(input())
arrays = []

for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    arrays.append(arr)

total_similarity = 0

for i in range(n):
    for j in range(i + 1, n):
        similarity = calculate_similarity(arrays[i], arrays[j])
        total_similarity += similarity

print(total_similarity)
