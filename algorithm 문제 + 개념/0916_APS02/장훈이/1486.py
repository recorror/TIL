import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))
    # 부분집합 구하는 반복문
    arr = [[]]                      # 공집합
    for i in Hi:                    # i 번째 원소
        for j in range(len(arr)):       # 다 추가할 때까지 len 값 계속 늘어남.
            arr.append(arr[j]+[i])  # i번째 원소를 포함한 값 추가
    # 부분집합의 합을 담을 empty list
    arr.pop(0)  # 공집합은 쓸모 없다.
    emp = []
    for i in range(len(arr)):
        if B <= sum(arr[i]):
            emp.append(sum(arr[i]))

    print(f'#{tc} {min(emp)-B}')