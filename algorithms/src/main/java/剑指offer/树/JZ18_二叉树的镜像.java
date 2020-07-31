package 剑指offer.树;

import 剑指offer.POJO.TreeNode;

/**
 * 题目描述
 * 操作给定的二叉树，将其变换为源二叉树的镜像。
 * 输入描述:
 * 二叉树的镜像定义：源二叉树
 *     	    8
 *     	   /  \
 *     	  6   10
 *     	 / \  / \
 *     	5  7 9 11
 *     	镜像二叉树
 *     	    8
 *     	   /  \
 *     	  10   6
 *     	 / \  / \
 *     	11 9 7  5
 *
 * @author: kfzx-menghj
 * @Time: 2020/7/31  12:11
 */
public class JZ18_二叉树的镜像 {
    public void Mirror(TreeNode root) {
        if (null == root) {
            return;
        }
        TreeNode tmp = null;
        tmp=root.left;
        root.left = root.right;
        root.right = tmp;

        Mirror(root.right);
        Mirror(root.left);
    }
}
