# write a program to print non repeated characters of a string
def string_char(string):
    lst=[]
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i]!=string[j] and string[i] not in lst and string[i]!=" ":
                lst.append(string[i])
    for i in lst:
        print(i,end=" ")
string=input("Enter a string:")
result=string_char(string)




         