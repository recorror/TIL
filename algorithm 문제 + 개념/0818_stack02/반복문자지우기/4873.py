import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    emp_sl = [0]

    for i in s:
        if emp_sl[-1] == i:
            emp_sl.pop()
        else:
            emp_sl.append(i)
    print(f'#{tc} {len(emp_sl)-1}')
