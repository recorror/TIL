import sys
sys.stdin = open('input.txt')

def sum_l(num):
    x = 0
    for sn in range(len(num)):
        x += num[sn]
    return x


T = int(input())

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
M = len(arr)
for tc in range(1, T+1):
    N, K = map(int, input().split())
    a_l = []
    last_l = []
    final_l = []
    for i in range(1, 1 << M):  # 1 << n : 부분 집합의 개수
        emp_l = []
        for j in range(M):      # 원소의 수만큼 비트를 비교함
            if i & (1 << j):    # i의 j번 비트가 1인 경우
                emp_l.append(arr[j]) # arr의 부분집합
        # print(emp_l)
        last_l.append(emp_l)
    # print(last_l)
    for ll in range(len(last_l)):
        if len(last_l[ll]) == N:
            final_l.append(last_l[ll])
    # print(final_l) #
    cnt = 0
    for y in range(len(final_l)):
        if sum_l(final_l[y]) == K:
            cnt += 1
    print(f'#{tc} {cnt}')