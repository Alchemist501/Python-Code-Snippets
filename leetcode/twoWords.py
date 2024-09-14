# Problem Description : https://leetcode.com/problems/merge-strings-alternately/description
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        if len(word1) > len(word2):
            small = len(word2)
            l = word1
        else:
            small = len(word1)
            l = word2
        for i in range(0, small):
            result += word1[i]
            result += word2[i]
        print(result)
        result += l[small:]
        print(result)
        return result


one = Solution()
one.mergeAlternately("cf", "eees")
