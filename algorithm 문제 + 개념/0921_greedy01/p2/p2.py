import sys
sys.stdin = open('input.txt')

'''
6자리 숫자에 대해서 완전 검색을 적용해서 baby-gin을 검사해보시오.
0~9 숫자 카드에서 임의의 카드 6장을 뽑았을 때 3장의 카드가 연속적인 번호를 갖는 경우를 run 이라하고, 
3장의 카드가 동일한 번호를 갖는 경우를 triple 라고 함.
6장의 카드는 run, triple로만 이루어져 있어야 Baby-gin임
'''

def f(i, k):
    if i == k:
        cnt = 0
        if arr[0] == arr[1] == arr[2]:
            cnt += 1
        if arr[0] + 1 == arr[1] == arr[2] - 1:
            cnt += 1
        if arr[3] == arr[4] == arr[5]:
            cnt += 1
        if arr[3] + 1 == arr[4] == arr[5] - 1:
            cnt += 1
        if cnt == 2:
            return True
        else:
            return False
    else:
        for j in range(i, k):
            arr[i], arr[j] = arr[j], arr[i]
            if f(i+1, k):
                return True
            arr[i], arr[j] = arr[j], arr[i]
        return False

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    if f(0, 6) == True:
        print(f'#{tc} True')
    else:
        print(f'#{tc} False')
