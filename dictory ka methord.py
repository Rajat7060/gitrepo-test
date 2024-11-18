x={'Name':'Anil', 'Age':26, 'exp':5}
print(len(x))
x.clear()
print(len(x))


y={'apple':'red','orange':'orange','mango':'yellow'}
a=y.copy()
print(a)


b={'cyon':1,'voilet':2,'green':3}
print(b.get('voilet'))
print(b.get('red'))



    
b={'cyon':1,'voilet':2,'green':3}
b.setdefault('voilet',10)
b.setdefault('red',10)
print(b)


b={'cyon':1,'voilet':2,'green':3}
z={'red':4,'white':5}
b.update(z)
print(b)
