#prime Number
num=int(input("Enter Number : "))
if num>1:
    if num==2:
        print(f'{num} is Prime')

    for i in range(2,num):
        if num%i==0:
            print(f'{num} is not Prime')
            break
        else:
            print(f'{num} is Prime')
            break
            
            

