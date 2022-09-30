import sys
sys.stdin = open('input.txt')
from collections import deque

def emergency_call(node):
    global result
    # 마지막 연락받은 사람들 중 가장 큰 값
    print(node)
    result = max(node)
    # 다음 연락 받을 사람들이 들어갈 리스트
    next_q = deque()
    # 현재 연락받은 사람들이 연락 할 사람들 찾기
    while node:
        n = node.pop()
        for i in node_d[n]:
            if visit[i] == 0:
                next_q.append(i)
                visit[i] = 1
    # if 연락 받을 사람이 있으면
    if next_q:
        emergency_call(next_q)

for tc in range(1, 11):
    N, start = map(int, input().split())    # N = 입력받는 데이터의 길이  # start = 시작 지점
    arr = list(map(int, input().split()))
    visit = [0] * 101                       # 방문 체크 리스트
    visit[start] = 1                        # 방문 체크
    result = 0
    node_d = {
        i:[] for i in range(1, 101)
    }  # 딕셔너리 형태로 key, value 맞춰줌.
    for i in range(0, N):
        if i % 2 == 0:
            # value 값 추가
            node_d[arr[i]].append(arr[i+1])
    # print(node_d)
    q = deque()
    q.append(start)
    emergency_call(q)

    print(f'#{tc} {result}')
