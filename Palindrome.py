import re

def isPalindrome(s: str) -> bool:

    fullText = s.lower().replace(" ","").strip()
    cleanText = re.sub(r'[^a-zA-Z0-9\s]', '', fullText)
    totalLength = len(cleanText) - 1
    finalResult = True

    for char in cleanText:
        if char != cleanText[totalLength]:
            finalResult = False
        totalLength -= 1

    return finalResult

print(isPalindrome("tab a cat"))