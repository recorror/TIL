import sys
sys.stdin = open('input.txt')

# 입력 값, 숫자는 int로 아니면 그냥 처리.
def chg_num(char):
    if char.isnumeric():
        return int(char)
    else:
        return char

def postorder(node):
    if len(arr[node]) == 2: # 숫자면 2, 연산자면 4
        return arr[node][1] # 양의 정수를 리턴
    else:
        if len(arr[node]) == 4:
            l = postorder(arr[node][2])
            r = postorder(arr[node][3])
            oper = arr[node][1]
            return calc(l,r,oper)

def calc(a, b, oper):
    calc_dict = {
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a//b,
    }
    return calc_dict[oper]

for tc in range(1, 11):
    N = int(input())        # 정점의 개수
    arr = [0,]              # root가 1부터 시작해서

    for _ in range(N):
        arr.append(list(map(chg_num, input().split())))

    result = postorder(1)
    print(f'#{tc} {result}')