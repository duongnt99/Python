m = input()
arr1 = list(map(int, input().split()))
n = input()
arr2 = list(map(int, input().split()))


arr3 = (list(set(arr1)-set(arr2)))
arr4 = (list(set(arr2)-set(arr1)))

arr5 = arr3 + arr4
arr5.sort() 
for x in range(len(arr5)):
    print(arr5[x])
"""arr4 = []
for x in range(len(arr1)):
    for y in range(len(arr2)):
        if(arr1[x] == arr2[y]):
            continue
        if( y == len(arr2)-1):
            if(arr1[x] != arr2[y]):
                print(arr1[x])"""
        
            






