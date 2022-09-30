import sys
sys.stdin = open('input.txt')
# 완전 이진트리
# 노드 번호가 i인 노드의 부모노드 번호 : i//2
# 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : 2*i
# 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : 2*i+1
# 레벨 n의 노드 번호 시작 번호 : 2**n

T = int(input())
for tc in range(1, T + 1):
    # N: 노드개수, M: 리프노드개수, L: 출력할 노드번호
    N, M, L = map(int, input().split())
    # 0 + 노드개수 만큼의 빈 리스트 tree
    tree = [0 for _ in range(N + 1)]
    node_arr = [list(map(int, input().split())) for _ in range(M)]
    # tree[L] = ?
    for i in range(len(node_arr)):
        tree[node_arr[i][0]] = node_arr[i][1]
    # print(tree) [0, 0, 0, 3, 1, 2]
    for i in range(N, 0, -1):
        #tree의 0번째 인덱스는 제외.
        if i // 2 > 0:
            tree[i//2] += tree[i]
    # print(tree) [0, 6, 3, 3, 1, 2]
    print(f'#{tc} {tree[L]}')