import sys
sys.stdin = open('input.txt')
"""
최적의 경로 구하는 문제 = BFS
다익스트라로 풀어볼것...!
같은 높이를 이동 = 1
다른 높이를 이동 = 1 + 높이의 차 
ex ) 0 -> 3 = 4만큼 연료 소비
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1000001
