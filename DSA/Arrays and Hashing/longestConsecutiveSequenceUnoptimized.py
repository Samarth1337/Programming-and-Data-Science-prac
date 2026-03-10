# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
#
# Input: nums = [1,0,1,2]
# Output: 3
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# nlogn solution

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        check = set()
        for i in nums:
            if i not in check:
                check.add(i)
        check_sort = sorted(check) #nlogn
        l = []
        l.append(nums[0])
        count = 1
        for i in range(1, len(check_sort)):
            if check_sort[i] - check_sort[i-1] == 1:
                l.append(check_sort[i])
                count = max(count, len(l))
            else:
                del l[:]
                # l.clear()
                l.append(check_sort[i])
        return count
