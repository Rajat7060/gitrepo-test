#table
x=int(input())
y = int(input())

for i in range(1,y+1):
    if i<=20 and i !=y :
        print("{} * {} = {}".format(x,i,x*i))#same ha ya
        #print("%d *%d = %d",%(x,i,x*i))
    elif i<=20 and i==y:
        print("%d * %d = %d"%(x,i,x*i))#same ha ya
        break
else:
    print("wrong")
        
