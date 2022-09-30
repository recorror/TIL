import sys
sys.stdin = open('input.txt')

patterns = {
        (2,1,1): 0, (2,2,1): 1, (1,2,2): 2, (4,1,1): 3, (1,3,2): 4,
        (2,3,1): 5, (1,1,4): 6, (3,1,2): 7, (2,1,3): 8, (1,1,2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    arr = sorted(list(set(arr)))[1:]          # 중복제거, 0만있는 부분 제거
    # print(arr)
    numbers = []
    res = 0
    for i in arr:
        key = format(int(i, 16), 'b')
        n1 = n2 = n3 = 0
        cnt = 0
        odd = 0
        even = 0
        temp = ''
        for i in range(len(key)):
            if key[i] == '1' and n2 == 0:
                n1 += 1
            elif key[i] == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif key[i] == '1' and n2 != 0:
                n3 += 1
            elif n3 != 0:
                cnt += 1
                r = min(n1, n2, n3)
                pw = patterns[(n1//r, n2//r, n3//r)]
                temp += str(pw)
                if cnt == 8:
                    if (odd * 3 + even + pw) % 10 == 0 and temp not in numbers:
                        res += odd + even + pw
                    numbers.append(temp)
                    odd = even = cnt = 0
                    temp = ''
                elif cnt % 2:
                    odd += pw
                else:
                    even += pw
                n1 = n2 = n3 = 0
    print(f'#{tc} {res}')