# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0:1}
        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            if diff in prefixSums:
                res += prefixSums[diff]
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res