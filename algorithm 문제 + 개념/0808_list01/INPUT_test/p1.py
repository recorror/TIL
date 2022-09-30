import sys
sys.stdin = open('input.txt')           # 표준 입력에 input.txt에서 연 파일을 넣겠다.

# number = int(input())                   # input은 Str type이다.
# res = '홀수' if number % 2 else '짝수'
# print(f'{res} 입니다.')

# 정수가 1개 이상이라면 공백으로 구분되서 입력되어 진다.
# 입력된 두 수를 더하시오.

# l = list(map(int, input().split()))
# print(l)
# for i in l:
#     print(i, type(i))

#여러 줄 입력이 있을 때
n_line = int(input()) # 반드시 입력 줄 수가 명시되어 있다.
lists = []
for _ in range(n_line):  #반복되는 횟수만큼 for 작성 이때 _는 반복될 때 숫자가 필요없는 경우.
    lists.append(list(map(int, input().split())))

print(lists)