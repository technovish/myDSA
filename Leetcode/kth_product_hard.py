from bisect import bisect, bisect_left
from math import ceil


class Solution:
    def kthproduct(self, nums1, nums2, k):
        def check(mid):
            total = 0
            for n1 in nums1:
                if n1 > 0:
                    total += bisect(nums2, mid // n1)
                elif n1 < 0:
                    pos = bisect_left(nums2, ceil(mid/n1)-1)
                    total += len(nums2) - pos

                else:
                    if mid >= 0:
                        total += len(nums2)
            return total

        left = -10**10
        right = 10**10

        while left < right:
            mid = (left+right) // 2

            if check(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left
    
s = Solution()
nums1 = [2, 5]
nums2 = [3, 4, 6]
k = 5
result = s.kthproduct(nums1, nums2, k)
print(result)  # Output: 21, as the products are [3, 4

