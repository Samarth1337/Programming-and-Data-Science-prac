# Implement Quicksort

# 912. Sort an Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
#
#
# Example 1:
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low: int, high:int):
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[i] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i
        def quickSort( low:int, high: int):
            if low < high:
                p = partition(low, high)
                quickSort(low, p-1)
                quickSort(p+1, high)
        quickSort(0, len(nums)-1)
        return nums
