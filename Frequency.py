l=int(input("Enter the length of the array: "))
arr=[]
for row in range(0,l):
    ele=int(input())
    arr.append(ele)
n=int(input("Enter element to be counted: "))
count=0
for i in range(len(arr)):
    if n==arr[i]:
        count=count+1
print(f'The number {n} appears {count} times in the list')