# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
#
# Input: nums = [1]
# Output: [1]
# Example 3:
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# Follow up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # There can only be 2 majority candidates that meet this condition freq > n/3
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0
        res = list()
        for i in nums:
            if candidate1 == i:
                count1 += 1
            elif candidate2 == i:
                count2 += 1
            elif count1 == 0:
                candidate1 = i
                count1 += 1
            elif count2 == 0:
                candidate2 = i
                count2 += 1
            else:
                count1 -=1
                count2 -=1
        count1 = 0
        count2 = 0
        threshold = len(nums)/3
        for i in nums:
            if i == candidate1:
                count1 += 1
            if i == candidate2:
                count2 += 1
        if count1 > threshold:
            res.append(candidate1)
        if count2 > threshold:
            res.append(candidate2)
        return res