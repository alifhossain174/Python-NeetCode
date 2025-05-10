class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstSet = set(s.lower())
        secondSet = set(t.lower())

        firstDict = dict()
        secondDict = dict()

        for characs in firstSet :
            firstDict[characs] = s.count(characs)

        for characs in secondSet :
            secondDict[characs] = t.count(characs)

        if len(firstDict) != len(secondDict) :
            return False

        status = 0
        for firstDictKey, firstDictValue  in firstDict.items() : 
            if firstDictKey in secondDict and secondDict[firstDictKey] == firstDictValue :
                status = 1
            else :
                status = 0
                break

        if status == 1 :
            return True
        else :
            return False