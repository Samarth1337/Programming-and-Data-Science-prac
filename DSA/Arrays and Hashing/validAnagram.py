# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_d1 = dict()
        str_d2 = dict()
        for char in s:
            if char in str_d1:
                str_d1[char] += 1
            else:
                str_d1[char] = 1
        for char in t:
            if char in str_d2:
                str_d2[char] += 1
            else:
                str_d2[char] = 1
        return str_d2 == str_d1