n=int(input("Enter value for n : "))
total=0
for n in range(1,n+1):
    if n%2==0:
        total+=n
print(f'Sum of even numbers upto {n} is {total}')