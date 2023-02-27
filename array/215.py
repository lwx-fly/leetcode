# Given an integer array nums and an integer k, return the kᵗʰ largest element
# in the array.
#
#  Note that it is the kᵗʰ largest element in the sorted order, not the kᵗʰ
# distinct element.
#
#  You must solve it in O(n) time complexity.
#
#
#  Example 1:
#  Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#
#  Example 2:
#  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
#  Constraints:
#
#
#  1 <= k <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#
#
#  Related Topics Array Divide and Conquer Sorting Heap (Priority Queue)
# Quickselect 👍 13250 👎 657
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        h=[nums[i] for i in range(k)]
        heapq.heapify(h)
        for i in range(k,len(nums)):
            #构建最小堆
            if nums[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h,nums[i])
        return heapq.heappop(h)



# leetcode submit region end(Prohibit modification and deletion)
