import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    house = list(map(int, input().split()))
    x = [-2, -1, 1, 2]
    res = 0
    for i in range(2, N-1):
        arr = []
        for j in x:
            if 0 <= i+j < N:
                arr.append(house[i+j])
        ma = max(arr)
        if ma < house[i]:
            res += house[i] - ma
    print(f'#{tc} {res}')