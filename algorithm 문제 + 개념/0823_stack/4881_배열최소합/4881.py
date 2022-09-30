import sys
sys.stdin = open('input.txt')

def powerset(x, y):
    for m in range()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    selected = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            x = arr[i][j]
            x = i
            y = j
            stack.append(powerset(x, y))
