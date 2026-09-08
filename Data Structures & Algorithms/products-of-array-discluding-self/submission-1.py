class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftList = [0] * n
        rightList = [0] * n
        res = [0] * n

        leftList[0] = 1
        rightList[n-1] = 1

        for i in range(1, n):
            leftList[i] = leftList[i-1] * nums[i-1]

        for i in range(n- 2 , -1, -1):
            rightList[i] = rightList[i+1] * nums[i+1]

        for i in range(n):
            res[i] = leftList[i] * rightList[i]
        return res

