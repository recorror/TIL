import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    #전체 쪽 수 P
    #A = A가 찾아야 할 페이지
    #B = B가 찾아야 할 페이지
    P, A, B = map(int, input().split())
    l = 1
    r = P
    cnt1 = 1
    # A의 경우
    while l <= r:
        c = int((l+r) / 2)
        if c == A:
            Pa = cnt1
            break
        else:
            if A < c:
                r = c
                cnt1 += 1
            elif A > c:
                l = c
                cnt1 += 1

    # B의 경우
    l = 1
    r = P
    cnt2 = 1
    while l <= r:
        c = int((l + r) / 2)
        if c == B:
            Pb = cnt2
            break
        else:
            if B < c:
                r = c
                cnt2 += 1
            elif B > c:
                l = c
                cnt2 += 1

    if Pa > Pb:
        print(f'#{tc} B')
    elif Pb > Pa:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')