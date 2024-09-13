items=['apple', 'banana', 'mango','mango' ,'orange','apple']
result=[]
for item in items:
    if item not in result:
        result.append(item)
    else:
        print("Duplicate : ", item)
