"""Now you are given a string S, which represents a software license key which we
would like to format. The string S is composed of alphanumerical characters and dashes.
The dashes split the alphanumerical characters within the string into groups.
(i.e. if there are M dashes, the string is split into M+1 groups).
The dashes in the given string are possibly misplaced."""
import re

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        tempStr = list(re.sub(r'\W+', '', S).upper())
        newStr = []
        strLen = len(tempStr)
        curIndex = 0

        while strLen > 0:
            toCut = K if (strLen % K == 0) else strLen % K

            tempBuff = []

            for i in range(curIndex, curIndex + toCut):
              tempBuff.append(tempStr[i])

            newStr.append(''.join(tempBuff))

            curIndex += toCut
            strLen -= toCut

        return '-'.join(newStr)

if __name__ == '__main__':
    i = "2-4A0r7-4k"

    s = Solution()

    print(s.licenseKeyFormatting(i, 4))
