import sys
sys.stdin = open('input.txt')

def f(r3, r4):
    global res
    if r3.count(0)<=7 or (r3.count(0)<=8 and max(r3)>=2) or (r3.count(0)<=9 and max(r3)>=3):
        for i in range(len(r3)-2):
            if r3[i] == r3[i+1] == r3[i+2] != 0:
                res = 1
                break
            elif max(r3)>=3:
                res = 1
                break
    elif r4.count(0)<=7 or (r4.count(0)<=8 and max(r4)>=2) or (r4.count(0)<=9 and max(r4)>=3):
        for i in range(len(r4)-2):
            if r4[i] == r4[i+1] == r4[i+2] != 0:
                res = 2
                break
            elif max(r4)>=3:
                res = 2
                break

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    for i in range(12):
        if i % 2 == 0:
            p1.append(arr[i])
        else:
            p2.append(arr[i])
    r1 = [0]*10
    r2 = [0]*10
    res = 0
    for i in range(6):
        r1[p1[i]] += 1
        r2[p2[i]] += 1
        print(p1, p2)
        print(r1, r2)
        f(r1, r2)


    if res == 1:
        print(f'#{tc} {res}')
    elif res == 2:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} {res}')