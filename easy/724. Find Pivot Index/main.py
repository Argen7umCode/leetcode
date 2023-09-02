class Solution:
    def pivotIndex(self, nums) -> int:
        left_sum, right_sum = 0, sum(nums)
        for index, item in enumerate(nums):
            right_sum -= item
            if right_sum == left_sum:
                if index != len(nums):
                    return index 
            left_sum += item
        else:
            return -1


s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
                