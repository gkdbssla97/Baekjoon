import sys

N = int(sys.stdin.readline().rstrip())

pick = list(map(int, sys.stdin.readline().split()))
cal = list(map(int, sys.stdin.readline().split()))

def dfs(cnt, result, plus, sub, mul, div):
    global max_result
    global min_result
    if cnt == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if plus:
        dfs(cnt + 1, result + pick[cnt], plus - 1, sub, mul, div)
    if sub:
        dfs(cnt + 1, result - pick[cnt], plus, sub - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * pick[cnt], plus, sub, mul - 1, div)
    if div:
        dfs(cnt + 1, -(-result // pick[cnt]) if result < 0 else result // pick[cnt], plus, sub, mul, div - 1)
max_result = -100000000001
min_result = 100000000001
dfs(1, pick[0], cal[0], cal[1], cal[2], cal[3])
print(max_result)
print(min_result)