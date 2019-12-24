my_dict = dict()
n = int(input())

for i in range(n):
    arr = list(input().strip().split())

    my_dict[arr[0]] = float(arr[1]),float(arr[2]),float(arr[3])

name = input()

TB = (my_dict[name][0] + my_dict[name][1] + my_dict[name][2])/3
print ('%.2f' % TB)
