class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        reuslts = []

        def dfs(i, path):
            #basecase
            if i == len(nums):
                reuslts.append(path.copy())
                return
            #actual backtrack
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)

        dfs(0, [])
        return reuslts
