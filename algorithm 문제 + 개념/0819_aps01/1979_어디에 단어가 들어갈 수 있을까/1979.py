import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    #  가로 범위
    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[x][y] == 1:
                cnt += 1
            if arr[x][y] == 0 or y == N - 1:
                if cnt == K:
                    res += 1
                if arr[x][y] == 0:
                    cnt = 0
    #  세로 범위
        cnt = 0
        for y in range(N):
            if arr[y][x] == 1:
                cnt += 1
            if arr[y][x] == 0 or y == N - 1:
                if cnt == K:
                    res += 1
                if arr[y][x] == 0:
                    cnt = 0

    print(f'#{tc} {res}')