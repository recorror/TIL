pattern = "is" # 찾을 패턴
text = "This is a book~!" # 전체 텍스트

def BruteForce(pattern, text):

    M = len(pattern) # 패턴의 길이
    N = len(text)    # 텍스트의 길이

    for idx in range(N - M + 1): # 텍스트의 길이만큼 순회. 순회 구간을 조금이라도 줄이는 범위.
        for jdx in range(M):     # 패턴의 길이만큼 순회.
            if pattern[jdx] != text[idx]:
                break
        else: # 패턴이 매칭된 상태. for else 문
            return idx
    else: # 탐색이 실패한 경우.
        return -1
