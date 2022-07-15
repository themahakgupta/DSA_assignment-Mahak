# to reverse an array in place
arr=[int(x) for x in input().split()]
def reverse_array(arr):
    if len(arr)!=0:
        print("The reversed array is:")
        for i in range(len(arr)):
            print(arr[(len(arr)-1)-i],end=" ")
    else:
        print("Array is empty!!")
result=reverse_array(arr)


