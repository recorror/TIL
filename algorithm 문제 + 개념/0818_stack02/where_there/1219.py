import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(T):
    tc, E = map(int, input().split())   # 테스트 케이스, 간선의 개수
    graph = [[]for _ in range(100)]     # 빈배열
    V = list(map(int, input().split()))

    #인접리스트
    for idx in range(0, len(V), 2):
        frm = V[idx]
        to = V[idx + 1]
        graph[frm].append(to)           # 단방향이기에 하나만

    start = 0                           # 시작 정점
    visited = [False for _ in range(100)]
    stack = []
    now = start                         # 현재 위치
    while stack:
        visited[now] = 1                # 방문 표시

        for nxt in graph[now]:          # 인접정점찾기
            if not visited[nxt]:
                stack.append(now)
                now = nxt
                break

        else:
            now = stack.pop()

    print(f'#{tc} {int(visited[99])}')