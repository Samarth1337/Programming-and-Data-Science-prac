# Encode and Decode Strings
# Solved
# Medium
# Topics
# Company Tags
# Hints
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:
#
# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }
# So Machine 1 does:
#
# string encoded_string = encode(strs);
# and Machine 2 does:
#
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
# Example 1:
#
# Input: dummy_input = ["Hello","World"]
#
# Output: ["Hello","World"]
#
# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2
#
# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:
#
# Input: dummy_input = [""]
#
# Output: [""]
#
# Constraints:
#
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.
#
# Follow up: Could you write a generalized algorithm to work on any possible set of characters?

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            length = len(word)
            encoded_str = encoded_str + str(length) + "#" + word
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        final = []
        if not str:
            return None
        i=0
        while i<len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            i = j + 1 + length
            final.append(word)
        return final