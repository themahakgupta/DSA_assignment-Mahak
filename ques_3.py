# to check that two strings are rotation of each other
def rotation_strings(str1,str2):
    temp1=str1+str1
    temp2=str2+str2
    if len(str1)!=len(str2):
        print("Strings are not rotation of each other!!")
    else:
        if str1 in temp2 and str2 in temp1:
            print("Strings are rotation of each other")
        elif str2 in temp1 :
            print("String second is rotation of string one")
        elif str1 in temp2:
            print("String one is rotation of string two")
        else:
            print("Strings are not rotation of each other")

str1=input("Enter first string:")
str2=input("Enter second string:")
output=rotation_strings(str1,str2)
