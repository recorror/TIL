import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ab = [list(map(int,input().split()))for i in range(N)]
    # print(ab)
    p = int(input())
    arr = []
    for j in range(p):
        cj = int(input())
        arr.append(cj)
    # print(arr)
    res = []
    for j in range(len(arr)):
        cnt = 0
        for i in range(len(ab)):
            if ab[i][0] <= arr[j] <= ab[i][1]:
                cnt += 1
        res.append(cnt)
    print(f'#{tc}',*res)