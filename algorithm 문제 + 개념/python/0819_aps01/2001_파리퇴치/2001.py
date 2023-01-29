import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v = 0
            # 해당 인덱스에서 MxM 범위 내 원소합을 저장
            for di in range(M):
                for dj in range(M):
                    sum_v += arr[i + di][j + dj]

