import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    code = input().split()
    stack = []
    for i in range(len(code)):
        if code[i].isdigit():
            stack.append(code[i])       # 숫자이면 스택
        if code[i] == '.':
            if len(stack) == 1:
                print(f'#{tc}',*stack)  # 마지막에 남아있는 스택을 출력
                break
            else:
                print(f'#{tc} error')
                break
        if len(stack) >= 2:             # 스택 길이가 1보다 클 때
            if code[i] in '+-*/':       # 연산자가 뒤에 오면
                b = int(stack.pop())
                a = int(stack.pop())
                if code[i] == '+':
                    stack.append(a+b)
                if code[i] == '*':
                    stack.append(a*b)
                if code[i] == '/':
                    stack.append(a//b)
                if code[i] == '-':
                    stack.append(a-b)   # 연산값을 저장해준다.
        else:                           # 스택 길이가 1일 때 연산자가 들어오면
            if code[i] in '+-*/':
                print(f'#{tc} error')
                break