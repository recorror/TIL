import sys
sys.stdin = open('input.txt')
'''
1번 열, 행은 모두 사무실.
사무실에서 출발 -> 관리구역 열이나, 행 중에 1개만 순회 -> 전부 순회 후 다시 사무실.
 1,2,3  3,2,1    || 1,3,2  3,2,1
 12,23,31 nP2
  arr[i][-2],arr[i][-1] == arr[j][0],arr[j][1]
'''
def f(i, k):
    if i == k:
        key = 0
        if emp[0] == 0:
            temp = emp + [0]
            # print(temp) # [0, 1, 2, 0] [0, 2, 1, 0]
            for c in range(len(temp)-1):
                key += arr[temp[c]][temp[c+1]]
            # 각 순열에 대해 key 값을 담아준다.
            min_l.append(key)
    else:
        for j in range(i, k):
            emp[i], emp[j] = emp[j], emp[i]
            f(i+1, k)
            emp[i], emp[j] = emp[j], emp[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    #  인덱스용 리스트 작성
    emp = [i for i in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    #  함수에서 받아올 값
    min_l = []
    f(0, N)
    result = min(min_l)
    print(f'#{tc} {result}')