s = 'Reverse this String.'

# 새로운 문자열에 담아준다.
reverse_s = ''
for i in range(len(s)-1, -1, -1):
    reverse_s += s[i]

print(reverse_s)

# 리스트로 변환해서 정렬한 후에 문자열로 반환.
list_s = list(s)
for idx in range(len(s) // 2):
    list_s[idx], list_s[-1-idx] = list_s[-1-idx], list_s[idx]
print(''.join(list_s))