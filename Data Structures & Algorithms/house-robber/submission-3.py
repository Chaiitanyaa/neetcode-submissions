class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        max_pay = [0] * n

        max_pay[0] = nums[0]
        max_pay[1] = max(nums[0], nums[1])

        for i in range(2, n):
            max_pay[i] = max(max_pay[i-1], (nums[i]+max_pay[i-2]))

        return max_pay[-1]
