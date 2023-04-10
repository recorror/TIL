import sys
sys.stdin = open('input.txt')
from itertools import combinations

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    S = []
    for i in range(N):
        for j in range(i, N):
            if i != j:
                S.append(arr[i][j] + arr[j][i])
    result = []
    emp = list(combinations(S, 2))
    for i in emp:
        i = list(i)
        print(i)
        # 푸는 중
