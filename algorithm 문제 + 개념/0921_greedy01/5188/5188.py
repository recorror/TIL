import sys
sys.stdin = open('input.txt')

def find_path(row, col):
    # 우측 끝에 도달한 경우
    if row == N - 1 and col == N - 1:
        return arr[-1][-1]

    #범위 안에서 돌게
    if row >= N or col >= N:                        # 더 이상 이동 x
        return 99999999999                          # 임의의 가장 큰 수를 리턴
    else:
        res_r = arr[row][col] + find_path(row+1, col)   # 현재위치+ 아래로 이동한 값
        res_c = arr[row][col] + find_path(row, col + 1) # 현재위치+ 오른쪽으로 이동한 값
        return res_r if res_r <= res_c else res_c

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = find_path(0, 0)
    print(f'#{tc} {res}')