a = [1,2,3,4,5,6,7,8,9,0]

for i in len(1<<a):
    for j in range(a):
        if i & (1<<j):
            print(a[j], end="")
        print()
    print()