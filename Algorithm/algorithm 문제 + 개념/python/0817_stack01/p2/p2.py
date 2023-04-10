import sys
sys.stdin = open('input.txt')

def push(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        else:
            cnt -= 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    A = input()
    push(A)
    if push(A) == 0:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {-1}')