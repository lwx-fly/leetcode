from typing import List


class Solution:
    # Find First and Last Position of Element in Sorted Array
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            # (]  1 2 3 4
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                elif nums[mid] == target:
                    right = mid
            if left == len(nums) or nums[left] != target:
                return -1
            return left

        def findRight(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                elif nums[mid] == target:
                    # Attention
                    left = mid + 1
            if left == 0 or nums[left - 1] != target:
                return -1
            return left - 1

        left = findLeft(nums, target)
        right = findRight(nums, target)
        if left == -1 or right == -1:
            return [-1, -1]
        return [left, right]
