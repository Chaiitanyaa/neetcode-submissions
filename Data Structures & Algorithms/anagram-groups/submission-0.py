class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedElems = {}


        for s in strs: 
            sortedWord = ''.join(sorted(s))
            if sortedWord in sortedElems:
                sortedElems[sortedWord].append(s)
            else:
                sortedElems[sortedWord] = [s]

        return list(sortedElems.values())

