import math;
def reverseString(s):
    listLength = math.floor(len(s)/2)
    tempString = ""
    print("listLength: ", s[0])
    for i in range(listLength):
           tempString = s[i]
           s[i] = s[listLength-1-i]
           s[listLength-1-i] = tempString
           tempString = ""
           
    
    return s

myList = ["n","e","e","t"]
print(reverseString(myList))