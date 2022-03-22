from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        # Input: nums = [1,3,5,6], target = 5 Output: 2
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                return mid
        return left
