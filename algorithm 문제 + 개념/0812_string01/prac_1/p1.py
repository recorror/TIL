import sys
sys.stdin = open('input.txt')
N = int(input())
for _ in range(N):
    # 슬라이싱
    # s = input()
    # s = s[::-1]
    # print(s)

    # 리스트를 이용해서 풀기.
    # s = list(input())
    # s.reverse()
    # print(''.join(s))

    # for문을 이용해 구현하기.
    s = list(input())
    sr = []
    for i in range(len(s)-1,-1,-1):
        sr.append(s[i])
    print(''.join(sr))