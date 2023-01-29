import sys
sys.stdin = open('input.txt')

def carrying(arr, emp):
    global res
    if arr and emp:
        a = arr.pop()
        b = emp.pop()
        if a <= b:
            res += a
            carrying(arr, emp)
        else:
            emp.append(b)
            carrying(arr, emp)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cont = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    cont = sorted(cont)
    truck = sorted(truck)
    res = 0
    if max(truck) <= min(cont):
        print(f'#{tc} 0')
    else:
        carrying(cont, truck)
        print(f'#{tc} {res}')