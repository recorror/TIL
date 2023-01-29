import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    dx = [-1, 1, 0] # 오른쪽이나 왼쪽으로 갈 경우
    dy = [0, 0, -1] # 위로 가는 경우
    for i in range(100):
        if arr[-1][i] == 2:
            col = i

    row = 99
    while row > 0:
        for idx in range(3):
            next_row = row + dy[idx]
            next_col = col + dx[idx]
            if 0 <= next_row < 100 and 0 <= next_col < 100:
                if arr[next_row][next_col] == 1:
                    arr[row][col] = 0
                    #   현재 값이 1이면 본인을 계속 다음 값으로 인식함.
                    row = next_row
                    col = next_col
    print(f'#{tc} {col}')