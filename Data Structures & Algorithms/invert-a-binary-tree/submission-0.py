# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node):
            node.left,node.right = node.right,node.left
            return node
        if root:
            st = [root]
            while st:
                el = st.pop()
                node = swap(el)
                if el.left:
                    st.append(node.left)
                if el.right:
                    st.append(node.right)
        return root
        