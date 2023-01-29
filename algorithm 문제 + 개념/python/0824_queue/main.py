import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc = input()
    q = list(map(int, input().split()))

    num = 1
    while q[-1] > 0:
        pw = q.pop(0)
        pw -= num
        q.append(pw)
        num += 1
        if num == 6:
             num = 1

    q[-1] = 0
    print(f'#{tc}',*q)