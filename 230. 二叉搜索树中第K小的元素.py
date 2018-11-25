# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        lis=self.midTraverse(root=root)
        # print(lis)
        # lis.sort()
        return lis[k-1]

    # def midTraverse(self,root,lis=[]):
    def midTraverse(self, root):
        if not root:
            return []
        lis=[]
        lis.extend(self.midTraverse(root.left))
        lis.append(root.val)
        lis.extend(self.midTraverse(root.right))
        return lis

class node():
    def __init__(self, k=None, l=None, r=None):
        self.val = k
        self.left = l
        self.right = r

    def listcreattree(self,root,llist,i):###用列表递归创建二叉树，
        if i<len(llist):
            if llist[i] =='null':
                return None ###这里的return很重要
            else:
                root=node(k=llist[i])
                root.left= self.listcreattree(root.left, llist, 2 * i + 1)
                root.right=self.listcreattree(root.right, llist,2*i+2)
                return root  ###这里的return很重要
        return root
if __name__ == '__main__':
    root=node()
    llist = [4,2,5,1,3]
    root = root.listcreattree(root, llist, 0)

    a=Solution()
    print(a.midTraverse(root=root))
    print(a.kthSmallest(root,5))