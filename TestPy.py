import math
print("Giai phuong trinh bac 2");

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

delta= b*b-4*a*c
print("Delta la: ", delta)

if(delta<0):
    print("Phuong trinh vo nghiem")
elif(delta==0):
    Nghiem = (-b)/(2*a)
    print("Phuong trinh co nghiem kep: ", Nghiem)
else:
    Nghiem1 = (-b + math.sqrt(delta))/(2*a)
    Nghiem2 = (-b - math.sqrt(delta))/(2*a)
    print("Nghiem thu nhat: " , Nghiem1)
    print("Nghiem thu hai: " , Nghiem2)
 
# Dòng lệnh này nằm ngoài khối lệnh for.
print("End of example");