import math

# print(math.sqrt(2))

# # ceilは大きい方にまとめられる
# print(math.ceil(3.2)) # 4
# print(math.ceil(5.0))   # 5
# print(math.ceil(-2.7))  # -2  （-2 > -2.7)

# # floorは小さい方にまとめられる
# print(math.floor(3.2))   # 3
# print(math.floor(5.0))   # 5
# print(math.floor(-2.7))  # -3  （-3 < -2.3）


a = tuple([1,2,3])
b = [2,1,3]
c = tuple([3,1,2])

cycles = set()
cycles.add(a)
cycles.add(tuple(sorted(b)))
cycles.add(c)

print("セットの中身:", cycles)
