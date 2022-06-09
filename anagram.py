def anag(s1,s2):
    if(len(s1)&len(s2)==0):
        return("enter valid sttrings")
    elif(sorted(s1)==sorted(s2)):
        return("the given strings are anagram")
    else:
        return("the given strings are not anagram")

j=input("Enter the string")
k=input("Enter the string")
print(anag(j,k))


