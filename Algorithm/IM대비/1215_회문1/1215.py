import sys
sys.stdin = open('input.txt')

def pelin(str):
    a = str
    b = list(reversed(str))
    if a == b:
        return True
    else:
        return False

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    res = 0
    #행에 회문이 있을 경우
    for i in range(8):
        for j in range(8):
            x = arr[i][j:j+N]
            # 길이가 N이고 회문이라면 res += 1
            if len(x) == N and pelin(x):
                res += 1
    #arr의 전치행렬 emp
    emp = []
    for m in range(8):
        y = []
        for n in range(8):
            y.append(arr[n][m])
        emp.append(y)
    # 전치행렬의 행에 회문이 있을 경우
    # 즉, 열에 회문이 있을 경우
    for i in range(8):
        for j in range(8):
            z = emp[i][j:j + N]
            # 길이가 N이고 회문이라면 res += 1
            if len(z) == N and pelin(z):
                res += 1
    print(f'#{tc} {res}')