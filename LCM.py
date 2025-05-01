a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

maxnum = max(a,b)
while True:
    if (maxnum%a == 0 and maxnum%b ==0):
        break
    maxnum = maxnum +1

print(f"LCM of {a} and {b} is {maxnum}")