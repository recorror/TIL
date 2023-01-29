import sys
sys.stdin = open('input_bus.txt')
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
T = int(input())
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
for _ in T:
    K, N, M = int(input().split())
    bus_stop = int(input().split())
    for i in range(M):
                     