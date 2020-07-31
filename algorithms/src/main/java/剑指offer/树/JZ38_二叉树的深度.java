package 剑指offer.树;

import 剑指offer.POJO.TreeNode;
/**
 * JZ38_二叉树的深度
 * 题目描述
 * 输入一棵二叉树，求该树的深度。
 * 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
 *
 * @author: kfzx-menghj
 * @Time: 2020/7/31  10:55
 */
public class JZ38_二叉树的深度 {
    public int TreeDepth(TreeNode root) {
        if (null == root) {
            return 0;
        }
        int leftDepth = TreeDepth(root.left) + 1; //迭代一次算一层深度
        int rightDepth = TreeDepth(root.right) + 1;
        return leftDepth>rightDepth?leftDepth:rightDepth; //左树和右树，取深度大的
    }
}
