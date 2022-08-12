p = "is" # 찾을 패턴
t = "This is a book~!" # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N: # 각각의 길이를 초과하지 않게.
        if t[i] != p[j]: # 만약 패턴의 길이가 다르다면
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M # 검색 성공
    else: return -1 # 검색 실패

print(BruteForce(p, t)) # 패턴의 길이는 얼마인가?