s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

# 비교 ==
print(s1 == s2) # True
print(s1 == s3) # False
print(s1 == s4) # True
print(s1 == s5) # True
print('='*10)
print(s2 == s3) # False
print(s2 == s4) # True
print(s2 == s5) # True
print('='*10)
print(s3 == s4) # False
print(s3 == s5) # False
print('='*10)
print(s4 == s5) # True
print('='*10)

# 비교 is
print(s1 is s2) # True
print(s1 is s3) # False
print(s1 is s4) # True
print(s1 is s5) # False
print('='*10)
print(s2 is s3) # False
print(s2 is s4) # True
print(s2 is s5) # False
print('='*10)
print(s3 is s4) # False
print(s3 is s5) # False
print('='*10)
print(s4 is s5) # False