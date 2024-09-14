# Problem Description : https://leetcode.com/problems/merge-sorted-array/description
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        length = m + n
        while len(nums2) != 0 and i < length:
            x = nums1[i]
            y = nums2[j]
            if x < y:
                i += 1
            elif x >= y:
                nums1.insert(i, y)
                nums2.pop(j)
                nums1.pop(length)
                i += 1
        for k in range(length - 1, -1, -1):
            if len(nums2) == 0:
                break
            if nums1[k] == 0:
                nums1[k] = nums2[len(nums2) - 1]
                nums2.pop(len(nums2) - 1)


s1 = Solution()
s1.merge([2, 0], 1, [1], 1)
