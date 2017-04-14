"""
LeetCode #459

Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only
and its length will not exceed 10000.

Example:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return False

        s1 = (s + s)[1:-1]

        return s1.find(s) != -1

if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern("abab"))
    print(s.repeatedSubstringPattern("aba"))
