import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):   # 슬라이싱으로 풀 수는 없을까?
            box[j] = i

    print(f'{tc}', *box)