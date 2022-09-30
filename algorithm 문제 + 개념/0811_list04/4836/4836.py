import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    paper = [[0 for _ in range(10)] for _ in range(10)]

    N = int(input())
    for nc in range(1, N+1):
        r1,c1,r2,c2,color = map(int, input().split())
        cnt = 0
        for x in range(r1,r2+1):
            for y in range(c1,c2+1):
                if paper[x][y] == 1 or paper[x][y] == 2:
                    cnt += 1
                else:
                    paper[x][y] = color
    print(f'#{tc} {cnt}')