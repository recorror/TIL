import sys
sys.stdin = open('input.txt')

def Palindrome(arr, N, M):

    #열으로 (M-1)만큼 이동하며 조사
    for i in range(N):                              # 'asdad'
        for j in range(N-M+1): # 5, 3이라고 가정     # 'asdas'
            text = arr[i][j:j+M]                    # 'dfsfd'
            if text == text[::-1] :                 # 'sdfaw'
                return text                         # 'qweax'

    #행으로 (M-1)만큼 내려가며 조사
    for j in range(N):
        for i in range(N-M+1):
            text = ''
            for k in range(M): # M = 3
                text += arr[i+k][j]   # k =0,1,2       #text = aad
            if text == text[::-1]:
                return text

T = int(input())
for tc in range(1, T+1):
    N , M = map(int, input().split())
    arr = [input() for _ in range(N)]
#['asdad',t
# 'asdas',
# 'dfsfd',
# 'sdfaw',
# 'qweax']

    print(f'#{tc} {Palindrome(arr,N,M)}')