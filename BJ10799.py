import sys

pipe = list(sys.stdin.readline().rstrip())

result =[]
cnt = 0
answer = 0

for i in range(len(pipe)):
    if pipe[i] == "(":
        result.append(pipe[i])
    elif pipe[i] == ")":
        if pipe[i - 1] == "(": # Lazer
            result.pop()
            answer += len(result)
        else: # ))일경우 쇠파이프의 끝단
            result.pop()
            answer += 1

print(answer)