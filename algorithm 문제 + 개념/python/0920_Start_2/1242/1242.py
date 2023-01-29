import sys
sys.stdin = open('input_test.txt')

def scanner(arr):
    total = 0
    for row in range(N):
        # 1자리의 16진수가 M개 있는데 이 16진수를 2진수 4자리로 변경했기 때문에 M*4
        # index 탐색을 할 것이기에 -1까지
        col = M * 4 - 1     # M의 값은 유동적이다.
        while col >= 55:    # 55 번째의 리스트의 값이 1이 아니라면 앞에는 암호코드가 존재하지 않는다.
            if arr[row][col] == '1':    # 마지막 자리가 1일 때
                for _ in range(8):      # 8자리 숫자 찾기
                    n2 = n3 = n4 =0     # 각 영역의 갯수를 카운팅

                    while arr[row][col] == '1': # n4 영역은 1로 구성되어짐.
                        n4 += 1
                        col -= 1

                    while arr[row][col] == '0': # n3 영역은 0으로 구성
                        n3 += 1
                        col -= 1

                    while arr[row][col] == '1': # n4랑 같음
                        n2 += 1
                        col -= 1

                    # 배율을 확인하기 위해 가장 작은 값을 찾고
                    # 그 값으로 해당 영역을 나눠주면 됨.
                    min_n = min(n2, n3, n4)
                    if min_n != 0:
                        code = patterns[(n2 // min_n, n3 // min_n, m4 // min_n)]
                        pwd.append(code)
patterns = {
    (2,1,1):0,
    (2,2,1):1,
    (1,2,2):2,

}
T = int(input())
for tc in range(1, T + 1):
    # N = 세로 , M = 가로
    N, M = map(int, input().split())
    # N*M 의 배열 ( arr )에는 16진수가 들어있음. > 2진수로 변환.
    arr = [''] * N
    for i in range(N):
        temp = input()
        bit = ''
        for j in range(M):  # 한 개씩 문자를 읽어옮
            # temp[j]        # 16진수 => 2진수로 바꿔야함.
            # int(x, base=16)    # 16진수를 10진수로 바꿔줌.
            # base 는 입력 받는 문자의 진수를 표현 !!
            val = f'{int(temp[j], base=16):04b}' # 2진수로 변환 완료.
            bit += val
        arr[i] = bit
