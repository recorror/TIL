def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]


size = 3
stack = [0] * size
top = -1

for i in range(1, size + 1):
    push(i, size)
print(stack)  #  [1, 2, 3]

for j in range(1, size + 1):
    print(pop())