# This solution passes only 9/16 test cases because it is the unoptimized approach (O(N)). If done using heap/trees/LLs, it can be brought down to O(log(N))
# Look for the sumRangeQuery1dMutableOptimized file to search for that approach.

# 307. Range Sum Query - Mutable
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, handle multiple queries of the following types:
#
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
#
# Example 1:
#
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
#
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

class NumArray:
    def __init__(self, nums: List[int]):
        self.l = len(nums)
        self.copy = nums
        self.prefix = [0] * (l + 1)
        for i in range(l):
            self.prefix[i + 1] = nums[i] + self.prefix[i]
        # print(self.prefix)

    def update(self, index: int, val: int) -> None:
        diff = val - self.copy[index]
        self.copy[index] = val
        for i in range(index, self.l):
            self.prefix[i + 1] += diff
        # print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        left += 1
        right += 1
        result = self.prefix[right] - self.prefix[left - 1]
        return result