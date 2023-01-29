import sys
sys.stdin = open('input.txt')

T = int(input())
for n in range(1, T+1):
    a, b = input().split()
    print(f'#{n} {len(a)-len(b)*a.count(b)+a.count(b)}')