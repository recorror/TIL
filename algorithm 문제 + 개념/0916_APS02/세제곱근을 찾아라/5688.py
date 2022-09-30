import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    # X**3 = N 이라면 X는 아무리 커도 N의 절반 보다는 작다.
    start = 1
    if N != 1:
        end = N // 2
    else:
        end = N
    res = -1
    while start <= end:
        X = (start + end) // 2
        if N == X ** 3:
            res = X
            break
        elif N < X ** 3:
            end = X - 1
        else:
            start = X + 1

    print(f'#{tc} {res}')