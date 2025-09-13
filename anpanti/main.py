def dfs(current, used, words, max_len):
    max_len[0] = max(max_len[0], len(current))
    for i, w in enumerate(words):
        if not used[i] and current[-2:] == w[:2]:
            used[i] = True
            dfs(current + w[2:], used, words, max_len)
            used[i] = False

def main(lines):
    n = int(lines[0])
    words = lines[1:]
    max_len = [0]
    used = [False] * n

    for i in range(n):
        used[i] = True
        dfs(words[i], used, words, max_len)
        used[i] = False

    print(max_len[0] if max_len[0] > 0 else -1)
