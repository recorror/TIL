import sys
sys.stdin = open('input.txt')

def DFS(num):
    global cnt, result

    if num >= N:            # 정류장에 도착한 경우.
        if result > cnt:
            result = cnt    # result값 return
        return

    if result < cnt:
        return

    start = num
    life = Data[start]

    for i in range(start+life, start, -1):
        cnt += 1
        DFS(i)
        cnt -= 1


TC = int(input())
for tc in range(1,TC+1):
    Data = list(map(int, input().split()))
    N = Data[0]
    result = 987654321
    cnt = 0
    DFS(1)
    print(f'#{tc} {result-1}')
