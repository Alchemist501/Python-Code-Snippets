# Problem Description : https://leetcode.com/problems/greatest-common-divisor-of-strings/description
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def d(large, small):
            if large.startswith(small):
                num = large.count(small)
                if small * num == large:
                    return small
                else:
                    return d(small, large[num * len(small) :])
            else:
                return ""

        l = len(str1)
        s = len(str2)
        large = str1
        small = str2
        if l == s:
            if small == large:
                return small
        if l < s:
            large = str2
            small = str1
            l = s
            s = len(small)
        print(d(large, small))
        return d(large, small)


s = Solution()
s.gcdOfStrings(
    "TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
)
