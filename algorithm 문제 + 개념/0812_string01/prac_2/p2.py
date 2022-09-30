import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())

    neg = False
    if N < 0:
        neg = True
        N = -N

    result = ''
    while N:
        N, remain = N // 10, N % 10
        result = chr(ord('0') + remain) + result

    if neg:
        print('-' + result)
    else:
        print(result)