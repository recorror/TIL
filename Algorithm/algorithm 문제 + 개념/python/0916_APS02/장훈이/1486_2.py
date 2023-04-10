import sys
sys.stdin = open('input.txt')
from itertools import combinations

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))
    arr = []
    # 공집합은 필요 없으니까 1부터.
    for i in range(1, N+1):
        emp = list(combinations(Hi, i))
        for j in emp:
            sum = 0
            for k in j:
                sum += k
            if sum >= B:
                arr.append(sum)
    res = sorted(arr)[0]-B
    print(f'#{tc} {res}')