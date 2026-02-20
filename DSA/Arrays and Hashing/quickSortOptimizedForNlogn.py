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

import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition3(low: int, high: int):
            p_idx = random.randint(low, high)
            pivot = nums[p_idx]
            nums[low], nums[p_idx] = nums[p_idx], nums[low]
            lt = low
            i = low
            gt = high
            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            return lt, gt

        def quickSort(low: int, high: int):
            if low < high:
                left, right = partition3(low, high)
                quickSort(low, left - 1)
                quickSort(right + 1, high)
        quickSort(0, len(nums) - 1)
        return nums
