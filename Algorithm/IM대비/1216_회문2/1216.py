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
    arr = [list(input()) for _ in range(100)]
    res = 0
    #행에 회문이 있을 경우
    for i in range(100):
        for j in range(100):
