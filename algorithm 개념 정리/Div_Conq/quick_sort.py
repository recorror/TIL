def quick_sort(arr):
    if len(arr) <= 1:           # 숫자가 1 이하일 때는 정렬할 필요가 없음.
        return arr

    left = []                   # 기준값 보다 작은 값을 저장
    right = []                  # 기준값 보다 큰 값을 저장
    pivot = arr[len(arr)//2]    # 가운데 값을 기준값으로 설정

    for i in range(len(arr)):
        if i == (len(arr)//2):    # 기준값이 비교되지 않도록 하기 위함.
            # left right 리스트에 들어갈 필요 없음
            # pivot 값이 기준 값이기 때문에 비교 대상으로 이미 정렬이 될 것임.
            continue
        if pivot > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [3,2,4,6,9,1,8,7,5,-1]
print(f'정렬 전 : ', numbers)
print('---'*12)
numbers = quick_sort(numbers)
print(f'정렬 후 : ', numbers)