'''
最长递增子序列长度
比如说输入 nums=[10,9,2,5,3,7,101,18]，其中最长的递增子序列是 [2,3,7,101]，所以算法的输出应该是 4。

'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 二分查找
    def lengthOfLIS_binaray(self, nums: List[int]) -> int:
        res = 0
        top = [0] * (len(nums))

        for i in nums:
            item = nums[i]
            left = 0
            right = res
            while left < right:
                mid = (left + right) // 2
                if top[mid] > item:
                    right = mid
                elif top[mid] < item:
                    left = mid + 1
                else:
                    right = mid
            if left == res:
                res = res + 1
            top[left] = item
        return res
