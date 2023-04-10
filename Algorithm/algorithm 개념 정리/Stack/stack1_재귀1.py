def f(i, N):
    if i == N:
        return
    else:
        print(i)    #재귀호출 전 단계에 할 일
        f(i+1,N)
                    #재귀호출 후에 할 일.
f(0, 3)