import sys
sys.stdin = open('input.txt')

def dfs(start):
    visit[start] = 1
    for i in adj[start]:
        if visit[i] == 0:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    '제출 안 한 사람도 1개의 "조"이다.'
    '첫번째 공집합 이외의 공집합은 포함시켜서 체크해야함.'
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for i in range(N+1)]
    for i in range(len(arr)):
        if i % 2 == 0:
            adj[arr[i]].append(arr[i+1])
            adj[arr[i+1]].append(arr[i])
    visit = [0]*(N+1)
    cnt = 0
    for i in range(1, len(adj)):        # 공집합 빼고 1부터.
        if visit[i] == 0:
            dfs(i)                      # 모든 경우의 수 체크
            cnt += 1                    # 경로 수 체크
    print(f'#{tc} {cnt}')