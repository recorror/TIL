num = [1,2,3,4,5]
N = len(num)

def comb(arr,n):
    result = []

    l = len(arr)

    if n == 0:
        return [[]]


    for i in range(l):
        elem = arr[i]
        for rest in comb(arr[i+1:],n-1):
            result.append([elem] + rest)
    return result



def perm(arr,n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in perm(arr[:i] + arr[i+1:], n-1):
            result.append([elem] + rest)
    return result