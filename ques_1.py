array=[int(x) for x in input().split()]
key=int(input("Enter the key value:"))
print("The input array is:",array)
print("The key value is:",key)
def two_sum(array,key):
    list=[]
    for i in range(len(array)):
        for j in range(len(array)):
            if(array[i]+array[j]==key and i!=j):
                list.append(array[i])
                list.append(array[j])
        return list
print("The pair of elements:",two_sum(array,key))

