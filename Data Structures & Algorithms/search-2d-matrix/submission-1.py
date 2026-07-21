class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right  = 0,len(matrix) - 1
        while left <= right:
            middle = (left + right) //2
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                left = 0
                right = len(matrix[middle]) -1
                while left <= right:
                    mid = (left + right) //2
                    if target == matrix[middle][mid]:
                        return True

                    elif target > matrix[middle][mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
            elif target > matrix[middle][0]:
                left = middle + 1

            else:
                right = middle -1
        return False
        
