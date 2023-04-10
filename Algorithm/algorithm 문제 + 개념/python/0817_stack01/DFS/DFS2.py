# 인접리스트 만들기
# visited 리스트
# DFS 시작
    # 방문처리
    # 인접한 점 중에서 방문 가능한 정점 찾기
    # 방문 가능하면 stack 넣고 방문
    # 방문 불가능 stack pop
import sys
sys.stdin = open('input.txt')

def DFS(now):               # 현재정점 now
    # 1. 방문표시
    visited[now] = 1
    result.append(now)      # 방문 경로 체크
    # 2. 인접 정점 확인
    for nxt in range(V + 1):
        if graph[now][nxt] == 1 and visited[nxt] == 0:
    # 3. 이동가능하다면 이동
            DFS(nxt)

V = 7                       #  정점의 개수
                            # 모든 경로를 받기
edge_list = list(map(int, input().split()))
E = len(edge_list) // 2     # 간선의 개수
#  인접행렬 만드는 부분
graph = [[0] * (V + 1) for _ in range(V + 1)]
for idx in range(E):
    # graph[start][end] = 1
    # graph[end][start] = 1
    frm = edge_list[idx * 2]
    to = edge_list[idx*2 + 1]
    graph[frm][to] = 1
    graph[to][frm] = 1


visited = [False] * (V + 1)
result = []
DFS(1)

print(result)