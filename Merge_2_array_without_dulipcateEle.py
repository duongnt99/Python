english = int(input())
arr = list(map(int, input().split()))
france = int(input())
arr1 = list(map(int, input().split()))

arr = set(arr)
arr1 = set(arr1)
print(arr.union(arr1))