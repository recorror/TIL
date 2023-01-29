import sys
sys.stdin = open('input.txt')

def scanner(arr):
    pwd = []
    for r in range(N):
        for c in range(M-1,-1,-1):
            # 0이 나온다면 1이 나올 때까지 반복.
            if arr[r][c] == '0':
                continue
            # 1이 나온다면 해당 자리부터 56개의 숫자를 가지고 암호문을 뽑아내면 됨.
            for pos in range(c - 56 + 1 , c, 7):
                num_bit = arr[r][pos:pos+7]     # 암호숫자비트
                pwd.append(patterns[num_bit])   # 암호 숫자를 담는다
            # 각 자리수의 합을 구한다.
            odd_num = 0
            even_num = 0
            for i in range(len(pwd)):
                if i % 2 == 0:
                    odd_num += pwd[i]
                else:
                    even_num += pwd[i]
            # 암호문을 만족하면 자리수 합을 리턴
            if (odd_num * 3 + even_num) % 10 == 0:
                return odd_num + even_num
            else:
                return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(arr)
    patterns = {
        '0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
        '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9,
    }

    res = scanner(arr)
    print(f'#{tc} {res}')
