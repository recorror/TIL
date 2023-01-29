import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    N = 100
    res = 1

    row_l = [input() for i in range(N)]
    print(row_l)