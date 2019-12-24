a1, b1, c1, a2, b2, a3 = map(float, input().split())
TB = float(((a1+b1+c1)+(a2+b2)*2+a3*3)/10)
if(float(TB) == int(TB)):
    print(int(TB))
else:
    print(TB)