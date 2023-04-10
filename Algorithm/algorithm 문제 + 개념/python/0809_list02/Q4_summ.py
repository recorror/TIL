import sys
sys.stdin = open('input_sum.txt')

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
T = int(input())
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

for tc in range(T):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    # ai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = []
    # N-M+1 = 8 > 마지막 인덱스 7,8,9
    for j in range(0, N - M + 1):
        # 구간 합 sum_num 초기화
        sum_num = 0
        # 구간의 길이만큼 반복하면서 값을 저장
        for i in range(M):  # M :0,1,2
            sum_num += ai[j + i]  # m 구간 만큼 더해준다.

        # 원하는 m만큼 더한 값 append
        x.append(sum_num)

    #  print(x)

    for j in range(len(x)):
        k = len(x) - j
        for h in range(1, k):
            if x[h-1] >= x[h]:
                x[h], x[h-1] = x[h-1], x[h]
    res = x[-1] - x[0]

    print(f'#{tc+1} {res}')