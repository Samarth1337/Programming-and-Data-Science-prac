# Longest Common Prefix
# Easy
# Topics
# Company Tags
# You are given an array of strings strs. Return the longest common prefix of all the strings.
#
# If there is no longest common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["bat","bag","bank","band"]
#
# Output: "ba"
# Example 2:
#
# Input: strs = ["dance","dag","danger","damage"]
#
# Output: "da"
# Example 3:
#
# Input: strs = ["neet","feet"]
#
# Output: ""
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] is made up of lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return res
            res += current_char
        return res
