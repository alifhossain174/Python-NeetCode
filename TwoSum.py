# Test input
nums=[2,5,5,11]
target=10

firstLoopIndex = 0
result = list()
for number in nums :
    
    if(len(result) == 2) :
        break

    secondLoopIndex = 0
    for secondNumber in nums : 
        if firstLoopIndex != secondLoopIndex and number + secondNumber == target :
            result.append(firstLoopIndex)
            result.append(secondLoopIndex)
            break
        secondLoopIndex += 1

    firstLoopIndex += 1

print(result)