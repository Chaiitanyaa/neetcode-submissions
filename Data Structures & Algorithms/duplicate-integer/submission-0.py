class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for num in range(len(nums)):
            
            if nums[num] in elements:
                return True
            elements.add(nums[num])
        return False
            