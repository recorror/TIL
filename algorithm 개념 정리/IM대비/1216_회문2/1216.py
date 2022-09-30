import sys
sys.stdin = open('input.txt')

def pelin(arr):
    for i in range(len(arr)):
        for j in range(len(arr), -1, -1):
            if arr[i] == arr[j]:


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))
    res = 0
    #행에 회문이 있을 경우
    pelin_l = []
    for i in range(99, -1, -1):
        emp = []
        for j in range(99-i+1):
            emp.append(arr[i][j])
            if pelin(emp)