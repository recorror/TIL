# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)


def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]


memo = [-1]*101
memo[0] = 0
memo[1] = 1
for i in range(101):
    print(i, fibo(i))

#  메모이제이션을 쓰지 않으면
#  중복호출이 많기 때문에 엄청 느리다.