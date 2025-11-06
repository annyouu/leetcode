N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())

    # 頂点Aから頂点Bへの辺を張る
    G[A].append(B)

# 頂点vごとに、終点頂点を番号順にして出力する
for v in range(N):
    G[v].sort()

    # 頂点vの隣接リストの頂点を順に出力
    for to in G[v]:
        print(to, end=' ')
    
    print()