import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [1]            # 0 번째, 이전 결과를 담고 있는 역할.
    print(*pascal)
    for _ in range(1, N):   # 0 번째는 이미 만들었으니까 1부터 시작.
        my_pascal = []
        my_pascal.append(1) # 왼쪽 끝에 1 추가

        # 중간에 계산한 이전 줄의 좌우 계산한 값
        for i in range(len(pascal) - 1):
            my_pascal.append(pascal[i]+pascal[i+1])
        # 우측 끝에 1추가
        my_pascal.append(1) # 우측 끝에 1추가

        pascal = my_pascal
        print(*pascal)