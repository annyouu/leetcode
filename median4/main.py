nums1 = [1, 4]
nums2 = [3, 5, 2]

merged = sorted(nums1 + nums2)

n = len(merged)

if n % 2 == 1:
    median = merged[n // 2]
else:
    median = (merged[n // 2 - 1] + merged[n // 2]) / 2

print(median)