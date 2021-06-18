from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> TreeNode:
            if preorder_left > preorder_right:
                return None
            root = TreeNode(preorder[preorder_left])
            inorder_root = inorder_dict[root.val]
            left_len = inorder_root - inorder_left
            right_len = inorder_right - inorder_root
            # 左子树
            # if left_len == 0:
            #     root.left = None
            # elif left_len == 1:
            #     root.left = TreeNode(inorder[inorder_left])
            # else:
            #     root.left = myBuildTree(preorder_left+1, preorder_left+left_len, inorder_left, inorder_root-1)
            # 简化
            root.left = myBuildTree(preorder_left+1, preorder_left+left_len, inorder_left, inorder_root-1)
            # 右子树
            # if right_len == 0:
            #     root.right = None
            # elif right_len == 1:
            #     root.right = TreeNode(inorder[inorder_right])
            # else:
            #     root.right = myBuildTree(preorder_left+left_len+1, preorder_right, inorder_root+1, inorder_right)
            # 简化
            root.right = myBuildTree(preorder_left+left_len+1, preorder_right, inorder_root+1, inorder_right)

            return root
        
        n = len(preorder)

        inorder_dict = {val: index for index, val in enumerate(inorder)}
        return myBuildTree(0, n-1, 0, n-1)