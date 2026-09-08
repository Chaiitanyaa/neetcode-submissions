class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countElem = {}

        for i in range(len(nums)):
            if nums[i] in countElem:
                countElem[nums[i]] += 1
            else:
                countElem[nums[i]] = 1

        sort = sorted(countElem, key=countElem.get, reverse=True)
        return sort[:k]
