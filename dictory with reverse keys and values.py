#Sample input

y = "1,4,3,2"

x = "10,40,30,20"

#Convert the input strings to lists of integers keys =list (map(int, datal.split(',')))
keys=list(map(int,y.split(',')))
values =list(map(int,x.split(',')))


#Create a dictionary from the keys and values data dict dict (zip (keys, values))

data_dict= dict(zip(keys,values))

#Print the dictionary in key order


print("dictionary with key order")
for key in sorted(data_dict.keys()):


    print (key, data_dict[key])

#Create a reverse dictionary for value order

reverse_dict={v: k  for k, v in (data_dict.items())}



#Print the dictionary in value order print("dictionary with value order")

for value in sorted(reverse_dict.keys()):

    print(value, reverse_dict[value])
