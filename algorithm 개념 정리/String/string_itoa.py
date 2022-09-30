def itoa(num):

    #음수인지 아닌지 판단
    neg = False  # flag : 음수라면 True, 양수라면 False
    if num < 0:
        neg = True
        num = -num

    result = ''
    while num:
        num, remain = num // 10, num % 10
        result = chr(ord('0') + remain) + result

    if neg:
        return '-' + result
    else:
        return result


s = 123
a = itoa(s)
print(a, type(a))