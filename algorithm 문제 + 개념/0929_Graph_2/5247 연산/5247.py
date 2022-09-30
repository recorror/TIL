import sys
sys.stdin = open('input.txt')
"""
최소 몇 번인가? = BFS
"""
# 선형 큐
def BFS(N, M):
    front = rear = -1 # Queue 의 시작을 위해 초기화
    calculated[N] = 1

    rear += 1
    Q[rear] = N

    while front != rear:        # 큐가 비어있는지 확인
        # Queue에서 꺼내기 (선형 큐 이기에 따로 삭제하지는 않을 것임.)
        front += 1
        num = Q[front]
        operator = [num + 1, num - 1, num * 2, num - 10]    # 4개의 계산된 결과가 나오게 됨.
        for i in range(4):
            if operator[i] == M: # 만들려는 M이 완성이 되었다면
                return calculated[num]

            if 0 < operator[i] <= 1000000:
                if calculated[operator[i]] == 0: # 아직 계산되지 않은 값이라면
                    calculated[operator[i]] = calculated[num] + 1
                    # Queue에 계산해야할 숫자를 추가
                    rear += 1
                    Q[rear] = operator[i]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 직접 Que를 직접 만들거나 collections 라이브러리의 deque를 이용해야 시간 안에 됨.
    Q = [0] * 1000001
    calculated = [0] * 1000001  # 몇 번 계산했는지 카운트를 이곳에 저장
                                # 인덱스는 계산된 값
    res = BFS(N, M)

    print(f'#{tc}', res)