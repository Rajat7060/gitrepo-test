# Get inputs for the first dictionary
data1 = list(map(int,input("data1: ").split(",")))
data2 = list(map(int,input("data2: ").split(",")))

# Get inputs for the second dictionary
data3 = list(map(int,input("data3: ").split(",")))
data4 = list(map(int,input("data4: ").split(",")))

dict1= dict(zip(data1,data2))
dict2= dict(zip(data3,data4))
print(dict1)
print(dict2)
# Concatenate the values from the two dictionaries based on common keys
result_dict = {}

for key in dict1:
    result_dict[key] = dict1[key]

# Add values from dict2 where keys match
for key in dict2:
    if key in result_dict:
        result_dict[key] += dict2[key]
    else:
        result_dict[key] = dict2[key]

# Prepare the concatenation result
c1= list(result_dict.items())
concatenation = [(int(k), v) for k, v in result_dict.items()]

# Print the result
print("concatenation:", concatenation)
print("check:", c1)
