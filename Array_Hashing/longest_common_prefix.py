# Longest Common Prefix
# Easy
# Topics
# Company Tags
# You are given an array of strings strs. Return the longest common prefix of all the strings.

# If there is no longest common prefix, return an empty string "".

# Example 1:

# Input: strs = ["bat","bag","bank","band"]

# Output: "ba"
# Example 2:

# Input: strs = ["dance","dag","danger","damage"]

# Output: "da"
# Example 3:

# Input: strs = ["neet","feet"]

# Output: ""


class Solution:
    def longestCommonPrefix(self, strs):
        common_prefix=""
        comparison_string=strs[0]
        for i in range(0, len(comparison_string)):
            for j in range(1, len(strs)):
                if comparison_string[i] != strs[j][i]:
                    return common_prefix
            common_prefix+=comparison_string[i]

        return common_prefix

    




strs = ["neet","feet"]
sol_instance=Solution()
print(sol_instance.longestCommonPrefix(strs))
