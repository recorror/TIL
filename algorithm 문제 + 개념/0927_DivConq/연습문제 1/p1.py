import sys
sys.stdin = open('input.txt')

def quick(arr):
    if len(arr) <= 1:               # 길이가 1개 이하일 때
        return arr

    left = []
    right = []
    pivot = arr[0]

    for i in range(1, len(arr)):    # 0번째를 pivot으로 삼았으니까 0번째는 비교 x
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    # 리턴값에서 재귀 돌면서 모두 정렬 !
    return quick(left) + [pivot] + quick(right)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    res = quick(arr)
    print(f'#{tc}',*res)