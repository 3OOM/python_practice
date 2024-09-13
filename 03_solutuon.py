# 5th iteration is skipped 
n=int(input("Enter vlaue : "))

for i in range(1,11):
    if i==5:
        continue
    print(f"{n} * {i}  = ",i*n)
    