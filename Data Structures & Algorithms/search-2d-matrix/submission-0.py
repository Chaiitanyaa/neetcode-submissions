class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        candidateRow = -1
        for r in range(rows):
            if matrix[r][0] <= target and target <= matrix[r][cols-1]:
                candidateRow = r
                break
        
        l = 0
        r = cols - 1
        while r >= l:
            mid = (l+r) // 2
            if target > matrix[candidateRow][mid]:
                l = mid + 1

            elif target <  matrix[candidateRow][mid]:
                r = mid - 1

            elif target == matrix[candidateRow][mid]:
                return True 

        return False

            