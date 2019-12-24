n = int(input())
matrix = [] 
  
for i in range(n): 

    matrix.append([input()]) 
      
    for j in range(0, 1): 
        matrix[i].append(input()) 

matrix.sort(key=lambda x:x[1],reverse=True)
print(matrix)       