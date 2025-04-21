# Problem:= https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def Insertion(nums: List[int], left, right) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = Insertion(nums, left, mid - 1)
            root.right = Insertion(nums, mid + 1, right)
            return root

        return Insertion(nums, 0, len(nums) - 1)
