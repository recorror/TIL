import sys
sys.stdin =open('input.txt')

def check(arr):
    arr.sort()
    for x in range(len(arr)):
        if x+1 < len(arr):
            if arr[x] == arr[x+1]:
                return False    # 중복이 있다.
            else:
                return True     # 중복이 없다.

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 가로열의 합이 45이고 중복이 없을 경우
    for i in range(9):
        emp = []
        for j in range(9):
            emp.append(arr[i][j])
        if sum(emp) == 45 and check(emp):
            cnt += 1
    # 세로열의 합이 45이고 중복이 없을 경우
    for i in range(9):
        emp = []
        for j in range(9):
            emp.append(arr[j][i])
        if sum(emp) == 45 and check(emp):
            cnt += 1
    # 3x3 배열 안의 합이 45이고 중복이 없을 경우
    for i in range(0,9,3):
        for j in range(0,9,3):
            emp = []
            for row in range(3):
                for col in range(3):
                    emp.append(arr[i+row][j+col])
            if sum(emp) == 45 and check(emp):
                cnt += 1
    # 조건을 만족할 때마다 1씩 증가
    # 가로+세로+3x3에서 각각 9씩 증가하기 때문에
    # 스도쿠가 완성이 되려면 조건을 충족하는 경우가 27가지여야함.
    if cnt == 27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')