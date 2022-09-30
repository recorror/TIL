import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    #덤프 횟수
    N = int(input())
    x = list(map(int, input().split()))
    for _ in range(N):
        x.sort()
        x[-1] -= 1
        x[0] += 1
    res = max(x)-min(x)

    print(f'#{tc} {res}')