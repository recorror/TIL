import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    testcase = [list(map(str, input()))for _ in range(5)]
    len_l = [len(testcase[i])for i in range(len(testcase))]
    ml = max(len_l)
    emp = ''
    for x in range(ml):
        for y in range(5):
            try:
                emp += testcase[y][x]
            except IndexError:
                continue
    print(f'#{tc} {emp}')