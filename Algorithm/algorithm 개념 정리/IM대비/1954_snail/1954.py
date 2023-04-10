import sys
sys.stdin = open('input.txt')

T = int(input())
cnt = 1
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    r, c = 0, 0
    ESWN = 0    # 동 남 서 북
    for i in range(1, N*N + 1):
        arr[r][c] = i
        r += di[ESWN]
        c += dj[ESWN]

        if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] != 0:
            r -= di[ESWN]
            c -= dj[ESWN]
            ESWN = (ESWN + 1) % 4 # 0, 1, 2, 3 반복
            r += di[ESWN]
            c += dj[ESWN]
    print(f'#{tc}')
    for j in arr:
        print(*j)