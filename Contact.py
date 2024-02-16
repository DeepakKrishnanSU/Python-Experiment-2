print('Enter the contact details')
Name=[]
Number=[]
for i in range(5):
    name, number = input().split()
    Name.append(name)
    Number.append(number)
Details=[tuple(Name),tuple(Number)]
print("Enter the person name to search")
search=input()
flag=0
index=-1
for ele in Details[0]:
    index=index+1
    if ele == search:
        flag=1
        break
if flag==1:
    Num=list(Details[1])
    print(Num[index])
else:
    print('Name not found')