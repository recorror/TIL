stackSize = 10
stack = [0] * stackSize
top = -1

top += 1            # 탑 증가
stack[top] = 1      # 스택에 push
                    # 줄을 넘어가면...
top += 1            # push(2)
stack[top] = 2


top -= 1
temp = stack[top + 1]
print(temp)

temp = stack[top]
top -= 1

stack2=[]
stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())