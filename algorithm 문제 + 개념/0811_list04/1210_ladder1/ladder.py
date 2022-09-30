import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    #마지막 줄에 2가 있는 곳이 당첨 지역.
    for col_x in range(100):
        if matrix[99][col_x] == 2:
            col = col_x

    # 좌, 우, 위 델타 why? 답을 알고있으니 답에서 시작점을 찾는게 쉽기 때문.
    # 최종 출력이 시작점. 시작점을 구하는 문제이기 때문.
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    row = 99
    while row != 0:  # 가장 윗부분에 도착하면 break
        # 방향 탐색 , 3방향
        for idx in range(3):
            next_row = row + dr[idx]
            next_col = col + dc[idx]

            if 0 <= next_row < 100 and 0 <= next_col < 100:  # 사다리 리스트 내부인지 확인
                if matrix[next_row][next_col] == 1:    # 이동할 수 있는 위치라면
                    matrix[row][col] = 0 # 있던 위치를 0으로 만들어야 되돌아가지 않음.
                    row = next_row
                    col = next_col
    print(f'#{tc} {col}')