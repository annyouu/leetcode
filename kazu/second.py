def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])


    # 左右をマージする
    result_merge = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result_merge.append(left[i])
            i += 1
        else:
            result_merge.append(right[i])
            j += 1
    
    if i < len(left):
        result_merge.extend(left[i:])
    if j < len(right):
        result_merge.e
    

# if i < len(left):
#         result_merge.extend(left[i:])
#     if j < len(right):
#         result_merge.extend(right[j:])