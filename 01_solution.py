numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
positive_numbers=[]
for num in numbers:
    if num>0:
        positive_numbers.append(num)    
print(positive_numbers)
print(f'Count of positive number is {len(positive_numbers)} ')