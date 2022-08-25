import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    x = m-1
    res = []
    for i in range(n-x):
        for j in range(n-x):
            emp = []
            for a in range(m):
                for b in range(m):
                    emp.append(arr[i+a][j+b])
            res.append(sum(emp))
    print(f'#{tc} {max(res)}')