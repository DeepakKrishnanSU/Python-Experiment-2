n=int(input("Enter the length of the array: "))
arr=[]
for row in range(0,n):
    ele=int(input())
    arr.append(ele)
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(f'The second greatest number = {arr[len(arr)-2]}')
print(f'The second smallest number = {arr[1]}')