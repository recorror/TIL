import sys
sys.stdin = open('test_1.txt')

def make_abs(num):
    if type(num)==type(1):
        if num >= 0:
            return num
        else:
            return -num

T = int(input())

for _ in range(1, T + 1):
    TC = int(input()) # TC * TC 배열
    line = [list(map(int, input().split())) for i in range(1, TC + 1)]
    # print(len(X_line)) =  x행의 수

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    sum = 0
    # 델타 배열 시작
    for x in range(TC):
        # print(len(X_line[x])) = y열의 수
        for y in range(TC):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < TC and 0 <= ny < TC: # 유효한 인덱스만 계산
                    a = make_abs(line[x][y] - line[nx][ny])
                    sum += a
    print(f'#{_} {sum}')