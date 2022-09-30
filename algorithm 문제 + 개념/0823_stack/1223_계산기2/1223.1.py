import sys
sys.stdin = open('input.txt')

# 후위표기식 만드는 함수
def step1(inOrder):

    order = {'+': 1, '*': 2}
    stack = []
    postOrder = []

    for token in inOrder:
        if token.isdecimal():
            postOrder.append(token)

        else:
            while len(stack) > 0 and order[stack[-1]] >= order[token]:  # stack에 값이 있고, 스택에 마지막 값의 우선순위가 token보다 높으면
                postOrder.append(stack.pop())                           # 우선순위가 높은 스택에 있는 값을 pop해서 postOrder에 추가
            stack.append(token)                                         # 그 후에 token을 append


    while stack:                                                        # stack에 남은 값들은
        postOrder.append(stack.pop())                                   # stack에 값이 빌때까지 postOrder에 추가


    return postOrder

# 연산 함수
def step2(postOrder):

    stack = []

    for token in postOrder:
        if token.isdecimal():               # 만약 토큰이 숫자면
            stack.append(int(token))        # 토큰을 정수로 변환해서 stack에 추가
        else:                               # 만약 토큰이 연산자면
            v1 = stack.pop()                # stack에 저장된 값(숫자)을 꺼내고
            v2 = stack.pop()
            if token == '+':                # '+' 연산
                stack.append(v1+v2)
            elif token == '*':              # '*' 연산
                stack.append(v1*v2)

    return stack[-1]

# a = '2+3*4+5'
#
# postOrder = step1(a)
# result = step2(postOrder)
#
# print(result)

T = 10
for tc in range(1, T+1):
    N = int(input())            # 테스트 케이스의 길이
    cal = input()

    postOrder = step1(cal)
    result = step2(postOrder)

    print(f'#{tc} {result}')