import sys
sys.stdin = open('input.txt')


def scanner(arr):
    total = 0
    for row in range(N):
        # 1자리의 16진수가 M개 있는데
        # 이 16진수를 2진수 4자리로 변경했기 때문에 M*4
        # index 탐색을 할 것이기에 -1 까지
        col = M * 4 - 1
        while col >= 55:  # 55 번째의 리스트의 값이 1이 아니라면 앞에는 암호코드가 존재하지 않음을 의미
            if arr[row][col] == '1' and arr[row-1][col] == '0':  # 마지막 자리가 1일 때
                pwd = []
                for _ in range(8):    # 8자리 숫자를 찾을 것임
                    n2 = n3 = n4 = 0  # 각 영역의 갯수를 카운팅

                    # 한 줄에 암호가 여러 개 있을 수 있기 때문에
                    # 다시 기준점이 되는 1 찾기
                    while arr[row][col] == '0':
                        col -= 1

                    while arr[row][col] == '1':   # n4 영역은 1로 구성되어짐
                        n4 += 1
                        col -= 1

                    while arr[row][col] == '0':   # n3 영역은 0으로 구성되어짐
                        n3 += 1
                        col -= 1

                    while arr[row][col] == '1':   # n2 영역은 1로 구성되어짐
                        n2 += 1
                        col -= 1

                    # 배율을 확인하기 위해 가장 작은 값을 찾고
                    # 그 값으로 해당 영역을 나눠주면 n2, n3, n4의 비율을 확인할 수 있음
                    min_n = min(n2, n3, n4)
                    if min_n != 0:
                        code = patterns[(n2 // min_n, n3 // min_n, n4 // min_n)]
                        pwd.append(code)

                if len(pwd) == 8:
                    even_sum = sum(pwd[::2])
                    odd_sum = sum(pwd[1::2])

                    if (odd_sum * 3 + even_sum) % 10 == 0:
                        total += even_sum + odd_sum       # 올바른 암호의 합을 구해야 함
            else:
                col -= 1

    return total


# (n2, n3, n4) : 숫자
patterns = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T+1):
    # N: 세로, M: 가로
    N, M = map(int, input().split())

    # N * M 의 배열에는 16진수가 들어있음
    # 2진수로 변환
    arr = [''] * N   # 변환한 2진수를 저장할 리스트
    for i in range(N):
        temp = input()

        bit = ''
        for j in range(M):  # 한 개씩 문자를 읽어옮
            # temp[j]  # 16진수 => 2진수로 바꿔야 함
            val = f'{int(temp[j], base=16):04b}'   # 2진수 문자로 변환 완료
            bit += val

        arr[i] = bit   # 한 줄씩 16진수를 2진수로 변환된 문자열이 저장됨

    res = scanner(arr)
    print(f'#{tc} {res}')