import sys

N = int(sys.stdin.readline())

lion = [[1 for _ in range(3)] for _ in range(N)]

for i in range(1, N):
    # 0 -> i-1칸에 사자 (0,0)
    lion[i][0] = (lion[i - 1][0] + lion[i - 1][1] + lion[i - 1][2]) % 9901
    # 1 -> i-1칸에 사자 (1,0)
    lion[i][1] = (lion[i - 1][0] + lion[i - 1][2]) % 9901
    # 2 -> i-1칸에 사자 (0,1)
    lion[i][2] = (lion[i - 1][0] + lion[i - 1][1]) % 9901
print(sum(lion[N-1]) % 9901)
