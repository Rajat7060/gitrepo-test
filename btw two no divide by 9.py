x = int(input())
y = int(input())

for i in range(x,y+1):
    print(i ,end=" ")
    if i%9==0:
        break
