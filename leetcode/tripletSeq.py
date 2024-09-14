# Problem Description : https://leetcode.com/problems/increasing-triplet-subsequence/description
class Solution(object):
    def increasingTriplet(self, nums):
        i = j = pow(2, 31)
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
