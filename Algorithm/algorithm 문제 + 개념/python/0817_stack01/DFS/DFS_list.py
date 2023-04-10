# 인접리스트 만들기
# visited 리스트
# DFS 시작
    # 방문처리
    # 인접한 점 중에서 방문 가능한 정점 찾기
    # 방문 가능하면 stack 넣고 방문
    # 방문 불가능 stack pop
import sys
sys.stdin = open('input.txt')

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
now = 1
stack = [now]
result = [1]

while stack:
    # 1. 방문을 한다.
    visited[now] = 1
    # 2. 인접 정점을 확인한다.
    for nxt in range(V + 1):
    # 3. 인접 정점을 이미 방문했는지 확인한다.
        if graph[now][nxt] == 1 and visited[nxt] == 0:
    # 4. 이동한다.
    # 4-1. 이전 경로를 stack에 넣는다.
            stack.append(now)
    # 4-2. 방문 정점을 변경한다.
            now = nxt
            result.append(nxt)
            break
    else:  #  이미 모든 정점이 방문 되었다면, stack에서 pop
        now = stack.pop()

print('-'.join(map(str, result)))