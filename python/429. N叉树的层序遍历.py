"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        currentStack=[root]
        res=[[root.val]]
        while currentStack:
            nextStack=[]
            v=[]
            for i in currentStack:
                for j in i.children:
                    if j:
                        nextStack.append(j)
                        v.append(j.val)
            currentStack=nextStack
            if v:
                res.append(v)
        return res