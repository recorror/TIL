import sys
sys.stdin = open('input.txt')

def bubble(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] >= lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

T = int(input())
for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    # print(str2)
    str1 = set(str1)
    str1 = list(str1)  #  중복 제거
    cnt_d = {}
    print(str1)
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str2[j] == str1[i]:  #  찾는 문자가 있을 때.
                cnt += 1
                cnt_d[str1[i]] = cnt
    # print(cnt_d) # {'Y': 2, 'X': 1, 'V': 1, 'P': 1}
    cnt_values = cnt_d.values()
    cnt_l = bubble(list(cnt_values))
    print(f'#{tc} {cnt_l[-1]}')