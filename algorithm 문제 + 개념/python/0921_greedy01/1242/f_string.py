
x = '2'
# base 는 입력 받는 문자의 진수를 표현
print('16진수: ', x)
y = int(x, base=16)  # base 의 기본값은 10
print('10진수: ', y)
z = f'{y:04b}'
# print(bin(y))  # 0b가 앞에 붙고 필요한 자리수만 나타나게됨
print(f'2진수: {z}')