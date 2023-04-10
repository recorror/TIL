import sys
sys.stdin = open('input.txt')

def find(n, arr):
    global cnt
    index = [i for i in range(len(arr))]
    if abs(lrcnt[1]-lrcnt[0]) < 2: # 번갈아가면서 찾을 수 있게 설정
        l = index[0]
        r = index[-1]
        m = index[(l + r) // 2]
        if arr[m] == n:
            cnt += 1
            return cnt
        else:   # A[m=4] = 5 오른쪽으로 탐사 진행.
            if arr[m] < n:     # 찾는 값이 중간보다 오른쪽에 있을 경우
                lrcnt[1] += 1
                find(n, arr[m+1:r])

            elif n < arr[m]:   # 찾는 값이 중간보다 왼쪽에 있을 경우
                lrcnt[0] += 1
                find(n, arr[l:m-1])
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))  # 정렬한 상태로 받아줌.
    print(A)
    B = list(map(int, input().split()))
    cnt = 0
    res = 0
    lrcnt = [0,0]           # 번갈아가면서 찾을 수 있게 설정
    for i in B:
        if i in A:          # B의 원소가 A의 원소이기도 한 경우에만 검사 ㄱ
            res += find(i, A)

    print(f'#{tc} {res}')