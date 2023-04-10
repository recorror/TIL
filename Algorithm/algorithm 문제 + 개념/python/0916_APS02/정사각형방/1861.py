import sys
sys.stdin = open('input.txt')

"""
상하좌우에 있는 다른 방으로 이동할 수 있다.
이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.
"""
def plus(start):
    cnt = 0
    stack = []
    # 1. start = (i, j)
    stack.append(start)
    while stack:            # 2. start = (nx, ny)
        x, y = stack.pop()  # @1. i, j => x, y // @2. nx, ny => x, y
        cnt += 1            # 진행시 cnt + 1
        for m in range(4):
            nx = dx[m] + x
            ny = dy[m] + y  # 범위 내에 있고 다음 값이 정확히 + 1이라면.
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] - arr[x][y] == 1:
                stack.append((nx, ny))  # 만족하는 값 없으면 while문 stop
    return cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    # print(arr)
    answer = [0, 0]
    for i in range(N):
        for j in range(N):
            # 튜플 형태로 // (0, 0), (0, 1), (1, 0), (1, 1)
            cnt = plus((i, j))
            if cnt > answer[1]:
                answer[1] = cnt             # cnt 가장 큰 값으로 계속 교체
                answer[0] = arr[i][j]       # 해당 자리의 값.
            elif cnt == answer[1]:          # 똑같은 큰 cnt 값이 여러개일 때.
                if arr[i][j] < answer[0]:   # 적힌 수 중 가장 작은 것.
                    answer[0] = arr[i][j]
    print(f'#{tc} {answer[0]} {answer[1]}')
