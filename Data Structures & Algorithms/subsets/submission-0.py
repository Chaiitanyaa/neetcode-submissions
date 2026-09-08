class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        #helper function for recursion
        def dfs(i, path):
            
            #break condition
            if i == len(nums):
                results.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)
            

        dfs(0, [])
        return results

            
