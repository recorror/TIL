import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    # print(left, right)
    return merge(left, right)
# 시간초과 해결해야함.
def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = merge_sort(arr)
    # print(res)
    print(f'#{tc} {res[len(res)//2]} {cnt}')