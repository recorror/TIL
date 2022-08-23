number = list(range(1, 6))  # 숫자
selected = [False] * len(number)
result = []

def powerset(idx): # 몇 번째 idx가 선택/선택되지 않았는지 고려하는 부분.

    if idx < len(number):       # 사용되는 숫자를 정할 수 있음.
        selected[idx] = True    # 사용되었을 때
        powerset(idx+1)         # 다음 자리 확인
        selected[idx] = False   # 사용되지 않았을 때
        powerset(idx+1)
    else:
                    # 부분 집합을 뽑아내는 부분
        res = []
        for i in range(len(number)):
            if selected[i]:
                res.append(number[i])

        result.append(res)

powerset(0)
print(result)