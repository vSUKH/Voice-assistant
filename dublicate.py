
   
list = [4,16,10,3,8,12,10,21,11,13,19,2,7,5,8]
unique = []
dublicate = []

for element in list:

    if element not in unique:
        unique.append(element)
    

    elif element not in dublicate:
        dublicate.append(element)


print(f"All elemnt is : ", list)
print(f"List of unique element is : ",unique)
print(f"Dublicate element is: ", dublicate)































