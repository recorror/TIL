import sys
sys.stdin = open('input.txt')

def preorder(V):
    if V != 0:
        print(V, end=' ')
        preorder(c1[V])
        preorder(c2[V])

def inorder(V):
    if V:
        inorder(c1[V])
        print(V, end=' ')
        inorder(c2[V])

def lastorder(V):
    if V:
        lastorder(c1[V])
        lastorder(c2[V])
        print(V, end=' ')

N = int(input())                        # 간선 수
emp = list(map(int, input().split()))   # 받아온 리스트
M = max(emp)                            # 자식 노드 중 가장 큰 값
p = []
for i in range(M+1):
    p.append(i)                         # 자식노드 중 가장 큰 값까지 인덱스 되어있는 부모 리스트
pl = len(p)
c1 = [0] + [0] * pl                     # 부모리스트의 크기만한 자식 1
c2 = [0] + [0] * pl                     # 부모리스트의 크기만한 자식 2
for i in range(len(emp)):
    if i % 2 == 0:                      # 부모 인덱스를 기준으로
        if c1[emp[i]] == 0:             # 자식1이 비어있으면
            c1[emp[i]] = (emp[i+1])
        else:                           # 자식1이 채워져있으면
            c2[emp[i]] = (emp[i+1])

print('전위 순회 :',end=' ')
preorder(1)
print()
print('중위 순회 :',end=' ')
inorder(1)
print()
print('후위 순회 :',end=' ')
lastorder(1)
print()
