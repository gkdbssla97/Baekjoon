from collections import deque

M = int(input())
jelly = []
visited = [[0] * M for _ in range(M)]

for i in range(M):
    jelly.append(list(map(int, input().split())))

dx = [0, 1] # Right Top
dy = [1, 0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        if jelly[x][y] == -1:
            print("HaruHaru")
            exit(0)

        for i in range(2):
            nx = x + dx[i] * jelly[x][y]
            ny = y + dy[i] * jelly[x][y]

            if 0<=nx<M and 0<=ny<M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])

    return print("Hing")

bfs(0, 0, visited)

# asdfasf
# asdfdas

