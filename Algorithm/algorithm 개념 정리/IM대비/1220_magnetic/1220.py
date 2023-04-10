import sys
sys.stdin = open('magnetic_input.txt')


EMPTY, N, S = 0, 1, 2

for test_case in range(1, 11):
    answer = 0
    lan = int(input())
    array = [list(map(int, input().split())) for _ in range(lan)]

    for row in range(lan - 1):
        for col in range(lan):
            if array[row][col] == N:
                # 아래칸이 S극이면, 교착 상태
                if array[row + 1][col] == S:
                    answer += 1
                elif array[row + 1][col] == EMPTY:
                    array[row + 1][col] = array[row][col]

    print('#' + str(test_case), answer)