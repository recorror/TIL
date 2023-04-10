# 선택 정렬 함수를 재귀적 알고리즘으로 작성해 보시오.

def SelectionSort(A, s):
    n = len(A)
    if s == n-1: return
    m = s
    for i in range(s, n):
        if A[m] > A[i]:
            m = i
    A[s], A[m] = A[m], A[s]

    SelectionSort(A, s+1)

A = [2, 4, 6, 1, 9, 8, 7, 0]
SelectionSort(A, 0)
print(A)