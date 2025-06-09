def removeDuplicates(nums) -> int:
    duplicates = list()
    unique = list()
    for number in nums:
        if number not in unique:
            unique.append(number)
        else:
            duplicates.append(number)

    index = 0
    for uniqueNumber in unique:
        nums[index] = uniqueNumber
        index += 1


    return len(unique)


myList = [1, 1, 2]
print(removeDuplicates(myList))