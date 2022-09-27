import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    arr = [0] + [0]*N
    for i in range(1, Q+1):
        l, r = list(map(int, input().split()))
        for j in range(l, r+1):
            arr[j] = i
    arr.pop(0)
    print(f'#{tc}',*arr)
