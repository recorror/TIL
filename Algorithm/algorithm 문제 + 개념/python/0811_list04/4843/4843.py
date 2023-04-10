import sys
sys.stdin = open('input.txt')

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

T = int(input())
for tc in range(1, T+1):
    ai = int(input())
    N = list(map(int, input().split()))

    N = bubble(N)
    new_l = []
    for n in range(5): # 10개까지 출력
        new_l.append(N[ai-1-n]) # 큰 값 먼저 담기
        new_l.append(N[n])         # 작은 값 큰값 다음에 담기

    print(f'#{tc}',*new_l)