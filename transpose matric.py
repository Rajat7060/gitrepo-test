r =  int(input())
c = int(input())
matrix=[]
print("row wise element")
for i in range(r):
    li= list(map(int,input().split(",")))
    matrix.append(li)
print("Matric: ",matrix)

ram = [[0]*r for _ in range(c)]
for i in range(r):
    ram = []
    for j in range(c):
        ram[j][i]= matrix[i][j]
    print(ram)
