# strs = ["onlyone"]
# strs = ["dog","racecar","car"]
# strs = ["bat","bag","bank","band"]
# strs = ["dance","dag","danger","damage"]
# strs = ["neet","feet"]
# strs=["","abc","abcd"]
# strs=["interview","internet","internal","interval"]
strs=["abcdef","abc","abcd"]

def longestCommonPrefix(strs) :

    if len(strs) == 1 :
        return strs[0]

    smallestWordLength = len(strs[0])
    currentLoopIndex = 0 
    smallestWordIndex = 0
    for str in strs :
        if str == "" :
            return ""
        if len(str) <= smallestWordLength :
            smallestWordLength = len(strs[currentLoopIndex])
            smallestWordIndex = currentLoopIndex
        currentLoopIndex += 1

    stringToCompare = strs[smallestWordIndex]
    for str in strs :
        finalMatchedString = ""
        for i in range(len(stringToCompare)) :
            if str[i] == stringToCompare[i] :
                finalMatchedString += str[i]
            else :
                stringToCompare = finalMatchedString
                break

    
    return stringToCompare

print(longestCommonPrefix(strs))