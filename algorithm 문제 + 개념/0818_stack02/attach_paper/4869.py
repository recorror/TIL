import sys
sys.stdin = open('input.txt')

def dp(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    elif N == 3:
        return 5
    elif N == 4:
        return 11
    return dp(N-1) + 2*(dp(N-2))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {dp(N // 10)}')



