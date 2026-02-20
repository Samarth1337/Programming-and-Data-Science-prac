# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
#
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

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
