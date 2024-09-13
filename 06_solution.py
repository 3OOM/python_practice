num=int(input("Enter value : "))
temp=num
fact=1
while(num>0):
    fact*=num
    num-=1
print(f"Factorial of {temp} is {fact}")