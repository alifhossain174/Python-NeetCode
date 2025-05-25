def reverseString(s):
    myCustomeList = []
    listLength = len(s)
    for character in range(len(s)):
        myCustomeList.append(s[listLength-1])
        listLength -= 1   
    
    counter = 0
    for character in range(len(myCustomeList)):
        s[counter] = myCustomeList[counter]
        counter += 1
    
    return s


myList = ["n","e","e","t"]
print(reverseString(myList))