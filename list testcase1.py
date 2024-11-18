# write yo9ur code here

d=input()

list1=list(map(int,d.split()))

print(list1)

c=0

x=int(input())
if 0<=x<len(list1)-1:
    while list1[x+1]>0:
        list1[x+1]//=10
        c+=1
    print(c)

else: print("Invalid Index")
