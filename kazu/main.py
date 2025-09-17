def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

s = list("cbbba")

even = [s[i] for i in range(0, len(s), 2)]
odd = [s[i] for i in range(1, len(s), 2)]

even = bubble_sort(even)
odd = bubble_sort(odd)

result = []
e_i = o_i = 0

for i in range(len(s)):
    if i % 2 == 0:
        result.append(even[e_i])
        e_i += 1
    else:
        result.append(odd[o_i])
        o_i += 1

print("".join(result))

