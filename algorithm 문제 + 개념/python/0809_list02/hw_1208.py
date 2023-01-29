import sys
sys.stdin = open('input_hw.txt')


def salt(lst):
    for n in range(len(lst)-1):
        for m in range(n+1, len(lst)):
            if lst[n] > lst[m]:
                lst[n], lst[m] = lst[m], lst[n]
    return lst


for _ in range(1, 11):
    n_dump = int(input())
    box_h = list(map(int, input().split()))
    for i in range(1, n_dump):
        salt(box_h)
        box_h[-1] -= 1
        box_h[1] += 1
    res = box_h[-1] - box_h[1]
    print(f'#{_} {res}')