# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.
#
# Note : If no such substring exists, return -1.
#
# Examples:
#
# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
# Input: s = "aaaa", k = 2
# Output: -1
# Explanation: There's no substring with 2 distinct characters.
# Input: s = "aabaaab", k = 2
# Output: 7
# Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
# Constraints:
# 1 ≤ s.size() ≤ 105
# 1 ≤ k ≤ 26

# Problem: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Issue: Doesn't work for cases like aab, k= 1 because set doesn't count frequency of characters, so it will return 2. Need to use a dictionary instead.
# class Solution:
#     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#
#         char_set = set()
#         left = 0
#         max_length = 0
#
#         for right in range(len(s)):
#             if s[right] not in char_set:
#                 char_set.add(s[right])
#
#             if char_set.__len__() > k:
#                 char_set.remove(s[left])
#                 left += 1
#             max_length = max(max_length, right - left + 1)
#         return max_length

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            char_map[char] = char_map.get(char, 0) + 1

            while len(char_map) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length