import sys
sys.stdin = open('input.txt')

def push(string):
    stack = []
    for i in string:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if not stack:
                return 0
            else:
                if i == ')' and stack.pop() != '(':
                    return 0
                elif i == '}' and stack.pop() != '{':
                    return 0
    if stack:
        return 0

    return 1



T = int(input())
for tc in range(1, T + 1):
    code = input()
    res = push(code)
    print(f'#{tc} {res}')