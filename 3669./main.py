import heapq

heap = [5, 3, 8, 1, 2]
heapq.heapify(heap) # ヒープ化
print(heap) # [1,2,8,5,3] (順序保証されないが、1が先頭に来る)

print(heapq.heappop(heap)) # 最小値を取り出して削除 1を出して削除
print(heap)                 # [2, 3, 8, 5]

heapq.heappush(heap, 0) # 0を先頭を追加する
print(heap) # [0, 2, 8, 5, 3]
print(heapq.heappop(heap)) # 最小値0を取り出して削除する。



# def prime_factors(n, k):
#     # 素因数分解する
#     factors = []
#     i = 2
#     temp = n
#     while i * i <= temp:
#         while temp % i == 0:
#             factors.append(i)
#             temp //= i
#         i += 1
#     if temp > 1:
#         factors.append(temp)
#     return factors
