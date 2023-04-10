import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N의 마지막 자릿수를 항상 0으로 만들어주어야 함.
    N = (int(input())//10)*10
    res = []
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{tc}')
    while N > 0:
        for m in money:
            if N % m != 0:
                res.append(N // m)
                N %= m
            else:
                res.append(N // m)
                N = 0
    print(*res)