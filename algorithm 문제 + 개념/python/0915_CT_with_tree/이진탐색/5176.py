import sys
sys.stdin = open('input.txt')

def inorder(V):
    # * 포인트 1 : 함수 내부에 cnt 정의 하면 재귀 돌면서 초기화 됨.
    global cnt
    # 배열이니까 범위 초과 안 하게 범위 설정.
    if V <= N:
        # 좌측 자식의 인덱스 ( 제일 왼쪽에 있는 곳까지 찾아감 )
        inorder(V*2)
        # 제일 왼쪽 밑에 있는 값부터 매겨진다.
        tree[V] = cnt
        # * 포인트 2 : 값 매겼으면 그 다음 값은 + 1 씩 올려줘야함.
        cnt += 1
        # 우측 자식의 인덱스
        inorder(V*2+1)
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 기준이 되는 배열 tree 생성
    tree = [0] * (N + 1)
    # 왼쪽 자식 < 루트 < 오른쪽 자식 == 중위 순회
    # 중위순회하면서 순회 루트대로 1씩 번호를 새겨준다.
    cnt = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')