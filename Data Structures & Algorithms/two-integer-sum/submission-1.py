class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elem = {}
        for i, v in enumerate(nums):
            compliment = target - v

            if compliment in elem:
                return [elem[compliment], i]

            elem[v] = i