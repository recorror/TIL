import sys
sys.stdin = open('input.txt')

def float2bin(f):
    cnt = 0
    res = ''
    a = 1
    while f:                # 0.625
        if f < 2 ** -a:
            res += '0'
        else:
            f -= 2 ** -a    # 0.625 > 2**-1(0.5)
            res += '1'
        cnt += 1
        if cnt > 12:
            return 'overflow'
        else:
            a += 1
    return res


T = int(input())
for tc in range(1, T + 1):
    N = input()     # 0.625  list
    S = float(N)    # 0.625  float

    print(f'#{tc} {float2bin(S)}')