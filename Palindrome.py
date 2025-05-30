import re
from math import ceil

def isPalindrome(s: str) -> bool:

    fullText = s.replace(" ","").strip()
    cleanText = re.sub(r'[^a-zA-Z0-9]', '', fullText.lower())

    totalLength = len(cleanText) - 1
    loopIteration = ceil(len(cleanText) / 2)
    finalResult = True

    for i in range(loopIteration):
        if cleanText[i] != cleanText[totalLength]:
            finalResult = False
            break
        totalLength -= 1

    return finalResult

print(isPalindrome("tab a cat"))