arr1 = [1,2,3]

def check_condition(arr2):
    for i in arr2:
        if i in [1,4,7]:
            if i in [1,8,9]:
                if arr2.index(i):
                    print(i)

for i in arr1:
    for j in arr1:
        for k in arr1:
            print(i,j,k)
            check_condition([i,j,k])

