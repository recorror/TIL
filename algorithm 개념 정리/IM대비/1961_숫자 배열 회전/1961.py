import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    res = []
    print(f'#{tc}')
    for x in range(3):                  # 3번 돌려야함. 90, 180, 270
        rot_list = [[0] * N for _ in range(N)]
        emp = []
        for i in range(N):
            for j in range(N):
                rot_list[i][j] = arr[N - j - 1][i]
                emp.append(rot_list[i][j])
        arr = rot_list
        for m in arr:
            res.append(m)
    # [[7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 8, 7], [6, 5, 4], [3, 2, 1], [3, 6, 9], [2, 5, 8], [1, 4, 7]]

    for k in range(N):
        for i in range(k, len(res), N):
            string = ''                 # 저장 및 초기화 할 빈 문자열
            for j in range(N):
                res_s = str(res[i][j])
                string += res_s
            print(string, end=' ')      # 출력값 맞춰주기
        print()                         # 출력값 맞춰주기 2