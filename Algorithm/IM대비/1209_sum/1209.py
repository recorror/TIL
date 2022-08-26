import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr =[list(map(int, input().split())) for _ in range(100)]
    #행의 합
    row = []
    for i in range(100):
        # 이 부분에서 초기화 해줘야 특정 부분만 구함.
        emp = []
        for j in range(100):
            emp.append(arr[i][j])
        row.append(sum(emp))
    a = max(row)
    #열의 합
    col = []
    for i in range(100):
        # 이 부분에서 초기화 해줘야 특정 부분만 구함.
        emp = []
        for j in range(100):
            emp.append(arr[j][i])
        col.append(sum(emp))
    b = max(col)
    #우대각 합
    r_side = []
    for i in range(100):
        for j in range(100):
            if i == j:  # 정확히 대각선 부분만 구하기 위함.
                r_side.append(arr[i][j])
    c = sum(r_side)
    # 좌대각 합
    l_side = []
    for i in range(100):
        for j in range(100):
            if i == j:  # 정확히 대각선 부분만 구하기 위함.
                l_side.append(arr[i][100-j-1])
    d = sum(l_side)
    print(f'#{tc} {max(a,b,c,d)}')