import sys
sys.stdin = open('input_mm.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    #  버블 정렬 시작
    for i in range(len(ai)):
        k = len(ai) - i
        for h in range(1, k):
            if ai[h-1] >= ai[h]:
                temp = ai[h-1]
                ai[h-1] = ai[h]
                ai[h] = temp
                #  버블 정렬 끝
    res = ai[-1]-ai[0] # max에서 min을 빼준다.
    print(f'#{_+1} {res}')