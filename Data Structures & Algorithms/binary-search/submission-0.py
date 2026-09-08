class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = (len(nums)-1)
        l = 0
        while l <= r:
            mid = r+l // 2
            # the targer value is somewhere in the right half
            if target>nums[mid]:
                l = mid + 1

            #the target value is in the left half
            elif target < nums[mid]:
                r = mid - 1

            elif target == nums[mid]:
                return mid

        return -1