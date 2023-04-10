import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_stop = [0] * 5001 # 5000개의 버스 정류장
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            bus_stop[j] += 1
    P = int(input())
    res = []
    for _ in range(P):
        C = int(input())
        res.append(bus_stop[C])

    print(f'#{tc}',*res)

