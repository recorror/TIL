import sys
sys.stdin = open('input.txt')

def preorder(V):
    global cnt
    if V:
        # print(V, end=' ')
        cnt += 1
        preorder(ch1[V])
        preorder(ch2[V])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    V_list = [i for i in range(V + 1)]
    print(V_list)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    print(arr)
    for j in range(len(arr)):
        if j % 2 == 0:
            if ch1[V_list[arr[j]]] == 0:
                ch1[V_list[arr[j]]] = arr[j+1]
            else:
                ch2[V_list[arr[j]]] = arr[j+1]
    print(ch1)
    print(ch2)
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')