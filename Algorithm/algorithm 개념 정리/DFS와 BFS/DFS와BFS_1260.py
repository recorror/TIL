import sys
sys.stdin = open('input.txt')
from collections import deque

def DFS(start):
    print(start, end=' ')
    visited1[start] = 1
    for i in adj[start]:
        if visited1[i] == 0:
            DFS(i)
            visited1[i] = 1

def BFS(start):
    q = deque([start])
    visited2[start] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in adj[now]:
            if visited2[i] == 0:
                q.append(i)
                visited2[i] = 1


N, M, start = map(int, input().split())
# 방문 표시 리스트.
visited1 = [0]*(N+1)
visited2 = [0]*(N+1)
# 인접 리스트
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
# 작은 값부터 출력하기 위한 sort
for i in range(len(adj)):
    adj[i].sort()
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
DFS(start)
print()
BFS(start)