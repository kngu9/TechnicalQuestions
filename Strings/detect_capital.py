"""
LeetCode #520

Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        b1 = True if word[0].isupper() else False
        b2 = True if not word[0].isupper() else False
        b3 = True if word[0].isupper() else False

        for i in range(1, len(word)):
            if not word[i].isupper():
                b1 = False
            else:
                b2 = False
                b3 = False

        return b1 or b2 or b3

if __name__ == '__main__':
    s = Solution()

    print(s.detectCapitalUse('USA'))
    print(s.detectCapitalUse('leetcode'))
    print(s.detectCapitalUse('Google'))
    print(s.detectCapitalUse('FlaG'))
