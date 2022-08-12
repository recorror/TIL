def pre_process(pattern):
    M = len(pattern) # 패턴의 길이

    skip_table = dict()
    for i in range(M-1): # 마지막 부분인 차피 가능성이 0이니까 그거보다 1칸 전까지.
        skip_table[pattern[i]] = M - i - 1
    return skip_table

def boyer_moore(text, pattern):
    skip_table = pre_process(pattern)
    M = len(pattern)

    i = 0 # text index
    while i <= len(text) - M:
        j = M - 1 # 뒤에서 비교해야 되기 때문에 j를 끝에 index로 설정
        k = i + (M - 1) # 비교를 시작할 위치 (현재위치 + M번째 인덱스)

        #비교할 j가 남아있고, 일치하면 그 다음 앞에글자를 비교하기 위해 인덱스 감소.
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1

        if j == -1: # 일치함.
            return i

        else:
            # i를 비교할 시작 위치를 skip table에서 가져온다.
            i = skip_table.get(text[i + M - 1], M)
