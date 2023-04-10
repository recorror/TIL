import sys
sys.stdin = open('test_2.txt')

# def sum_list(num):
#     sum_l = 0
#     for x in range(num):
#         sum_l += x
#     return sum_l

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr) # 원소 개수
    zip_ = 0
    real_list = []
    final_list = []
    for i in range(1, 1 << n): # 1 << n : 부분 집합의 개수
        list_a = []
        for j in range(n):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번 비트가 1인 경우
                list_a.append(arr[j])
        real_list.append(list_a)
    # print(real_list)
        for rl in range(len(real_list)):
            y = sum(real_list[rl])
            final_list.append(y)
            if final_list[rl] == 0:
                print(f'#{tc} 1')
                break
            else:
                print(f'#{tc} 0')