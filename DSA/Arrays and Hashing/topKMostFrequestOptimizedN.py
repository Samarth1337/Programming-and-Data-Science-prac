# 347. Top K Frequent Elements
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
#
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
#
# Output: [1]
#
# Example 3:
#
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#
# Output: [1,2]
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# o(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        for key, val in counts.items():
            buckets[val].append(key)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res