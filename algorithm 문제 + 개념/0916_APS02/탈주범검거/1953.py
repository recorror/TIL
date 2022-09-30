import sys
sys.stdin = open('input.txt')


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


T = int(input())
for tc in range(1, T+1):
    N,M,R,C,L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
