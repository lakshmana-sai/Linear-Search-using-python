def linear_Search(list1,key):
    found=False
    for i in range (0,len(list1)):
        if list1[i]==key:
            print("Element found at index:",i)
            found=True
    if found==False:
        print("Element not found")
print("Enter elements for perform linear search operation")
elements=input().split()
list1=list(map(int,elements))
key=int(input("Enter key value:"))
linear_Search(list1,key)
