english = int(input())
arr = list(map(int, input().split()))
france = int(input())
arr1 = list(map(int, input().split()))

arr = set(arr)
arr1 = set(arr1)

final = list(arr.difference(arr1))
print(len(final))