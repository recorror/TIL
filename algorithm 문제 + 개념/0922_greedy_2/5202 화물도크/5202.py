
# 백준 문제 // 시간초과 뜸...!
N = int(input())
emp = []
for _ in range(N):
    arr = list(map(int, input().split()))
    emp.append(arr)
emp = sorted(emp, reverse=True)
temp = []
for s, e in emp:
    temp.append([s, e])
    if len(temp) >= 2:
        for i in range(len(temp) - 1):
            if temp[i][1] == temp[i + 1][1] or temp[i][1] < temp[i + 1][1]:
                temp.pop()
            elif temp[i][0] < temp[i + 1][1]:
                temp.pop()
res = len(temp)
print(res)