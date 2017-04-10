"""
LeetCode #53
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    m = dp[0]

    for i in range(1, len(nums)):
        s = dp[i-1] + nums[i]

        dp[i] = max(nums[i], s)

        if dp[i] > m:
            m = dp[i]

    return m

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(arr))
