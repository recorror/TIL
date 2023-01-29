import sys
sys.stdin = open('input.txt')

def DFS(start, goal):               # 현재정점 now
    # 1. 방문표시
    stack = []
    result.append(now)      # 방문 경로 체크
    # 2. 인접 정점 확인
    for nxt in range(V + 1):
        if graph[now][nxt] == 1 and visit[nxt] == 0:
    # 3. 이동가능하다면 이동
            DFS(nxt)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
                                # V = 노드의 수, E = 간선의 수
    visit = [False] * (V + 1)   # 방문여부 확인
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for ec in range(E):
        S, G = list(map(int, input().split()))
        graph[S][G] = 1

    start, goal = map(int, input().split())
    n = DFS(start, goal)

    print(n)