import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    emp = []
    for i in range(abs(N-M)+1):             # 어느 쪽이 긴지 모르기 때문에 abs써줌.
        arr = []
        for j in range(min(N, M)):
            if N > M:
                arr.append(Ai[j+i]*Bj[j])   # Ai가 더 길 때
            else:
                arr.append(Bj[j+i]*Ai[j])   # Bj가 더 길 때
        emp.append(sum(arr))                # 자릿수끼리 곱한 값들을 sum
    print(f'#{tc} {max(emp)}')              # sum 값들 중 가장 큰 값 max로 뽑아줌.