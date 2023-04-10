import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    paper = [[0 for _ in range(10)] for _ in range(10)]
    count = 0  # 겹치는 칸의 개수
    N = int(input())
    for nc in range(1, N+1):
        r1,c1,r2,c2,color = map(int, input().split())
        cnt = 0
        for x in range(r1,r2+1):
            for y in range(c1,c2+1):
                if color == 1:  # 빨간색일 때
                    paper[x][y] += color
                else:  #  파란색일 때, 빨간색이 이미 칠해져 있을 때.
                    paper[x][y] += color
    # pprint(paper)
                if paper[x][y] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')