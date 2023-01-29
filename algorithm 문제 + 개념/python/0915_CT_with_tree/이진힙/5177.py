import sys
sys.stdin = open('input.txt')
#  완전 이진 트리에서 부모의 값 : i // 2

def min_heap(arr):
    for i in range(1, N + 1):
        while arr[i // 2] > arr[i]:
            arr[i // 2], arr[i] = arr[i], arr[i // 2]
            i = i // 2

T = int(input())
for tc in range(1, T + 1):                        # 자식이 부모보다 커야함.
    N = int(input())
    case = [0] + list(map(int, input().split()))  # [0, 7, 2, 5, 3, 4, 6]
    ch1 = [0] * (max(case) + 1)
    ch2 = [0] * (max(case) + 1)
    last = 0
    min_heap(case)
    # 조상노드의 합
    p = N // 2
    while p > 0:
        last += case[p]
        p = p // 2
    # print(case)
    print(f'#{tc} {last}')