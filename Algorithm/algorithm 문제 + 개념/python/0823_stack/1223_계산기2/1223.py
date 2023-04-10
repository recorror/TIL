import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    code = list(input())
    stack = []
    operator = []
    # 후위 연산자로 바꾸어주기.
    for i in range(len(code)):
        if code[i].isdigit():
            stack.append(int(code[i]))
        else:
            operator.append(code[i])
            if len(operator) > 1:
                if operator[-1] == '+':
                    if code[i] == '+':
                        stack.append(operator.pop())
                if operator[-1] == '*':
                    if code[i] == '+':
                        stack.append(operator.pop())
                    if code[i] == '*':
                        stack.append(operator.pop())
    stack.append(operator.pop())    # 가장 마지막에 1개 값이 남았을테니까 고거까지 딱 처리.
    print(stack)
    # 후위 연산자로 바꿔 준 값 stack을 계산.
