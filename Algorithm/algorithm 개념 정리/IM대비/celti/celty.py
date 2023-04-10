import sys
sys.stdin = open('input.txt')

def cnt_num(arr):
    emp = []
    col_num = [1,2,3,4,5,6,7,8,9,10]
    for i in range(n):
        for j in range(m):
            if arr[i][j] in col_num:
                emp.append(arr[i][j])
    emp.sort()
    max_num = []
    for i in emp:
        max_num.append(emp.count(i))
    print(emp[max_num.index(max(max_num))])
    print(max(max_num))

n, m = map(int, input().split())
N = int(input())
arr = [[0] * m for _ in range(n)]
for nc in range(N):
    x1, y1, x2, y2, color = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if arr[i][j] < color:
                arr[i][j] = color

cnt_num(arr)