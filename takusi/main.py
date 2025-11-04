import math

# # 小さい数（問題なし）
# x1 = 123456789.1
# print("ceil 小さい数:", math.ceil(x1))  # 123456790

# # 大きい数（誤差が出る可能性あり）
# x2 = 10**16 + 0.11  # 10000000000000000.1
# print("ceil 大きい数:", math.ceil(x2))  # 正しい結果は 10000000000000001 だが…

import math

# 整数の範囲で少し大きい割り算
x = 10**17 + 0.5  # 10^16 に微小な整数を足す
y = 3

# math.ceil を使う
ceil_val = math.ceil(x / y)

# 余り演算で安全に計算
x_int = int(x)
ceil_safe = x_int // y
if x_int % y != 0:
    ceil_safe += 1

print("x =", x)
print("math.ceil(x/y) =", ceil_val)
print("余り演算 ceil =", ceil_safe)
print("差 =", ceil_val - ceil_safe)

# # タクシー料金設定
# A = 400      # 初乗り料金
# B = 1        # 追加料金の距離単位
# C = 80       # 追加料金
# initial_km = 5  # 初乗り距離

# # 非常に大きな走行距離
# D = 10**15 + 0.1

# # math.ceilを使う
# extra_distance_ceil = max(0, D - initial_km)
# extra_units_ceil = math.ceil(extra_distance_ceil / B)
# total_ceil = A + extra_units_ceil * C

# # 余りを使った場合
# D_int = int(D)  # 超大きな距離を整数として扱う
# extra_distance_rem = max(0, D_int - initial_km)
# extra_units_rem = extra_distance_rem // B
# if extra_distance_rem % B != 0:
#     extra_units_rem += 1
# total_rem = A + extra_units_rem * C

# print("走行距離 D =", D)
# print("math.ceil を使った料金:", total_ceil)
# print("余り演算を使った料金:", int(total_rem))