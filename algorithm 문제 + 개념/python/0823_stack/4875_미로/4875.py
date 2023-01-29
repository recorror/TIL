import sys
sys.stdin = open('input.txt')

def dfs(y, x):
    global res
    arr[y][x] = 1   # 지나온 경로 1로 만들기
    for k in range(len(dx)):
        m = dx[k] + x
        n = dy[k] + y
        if 0 <= m < N and 0 <= n < N: # 범위 안일 때
            if arr[n][m] == 0:
                dfs(n, m)             # 0이면 재귀
            elif arr[n][m] == 3:      # 3에 도달하면 1 반환
                res = 1
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for n in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = j
                y = i
    res = 0
    dfs(y, x)

    print(f'#{tc} {res}')

