package 剑指offer.树;

import 剑指offer.POJO.TreeNode;

/**
 * 题目描述
 * 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
 *
 * 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
 * @author: kfzx-menghj
 * @Time: 2020/7/31  16:36
 */
public class JZ39_平衡二叉树 {
    public boolean IsBalanced_Solution(TreeNode root) {
        /**
         * 链接：https://www.nowcoder.com/questionTerminal/8b3b95850edb4115918ecebdf1b4d222?answerType=1&f=discussion
         * 来源：牛客网
         *
         * 1.判断树是否为空，空则返回true
         * 2.判断左右子树深度差，其中，求树深度的函数在上一题中“二叉树的深度中”已实现，差超过1，返回false
         * 3.若通过2的判断，对左右子树也判断是否都是平衡二叉树，判断函数为函数自身，递归调用
         */
        if (null == root) {
            return true;
        }
        if (Math.abs(getTreeDepth(root.left) - getTreeDepth(root.right)) > 1) {
            return false;
        }
        /**
         * 这两者都是表示逻辑与，只有当两边都是true时，返回true，只要有一个false则结果返回false。
         *
         *     &&还具有短路的功能，即如果第一个表达式为 false，则不再计算第二个表达式，例如，对于 if(str != null
         * && !str.equals(“”))表达式，当 str 为 null 时，后面的表达式不会执行，所以不会出现 NullPointerException
         * 如果将&&改为&，则会抛出 NullPointerException 异常。 If(x==33 & ++y>0) y 会增长， If(x==33 && ++y>0)
         * 不会增长
         * &还可以用作位运算符，当&操作符两边的表达式不是 boolean 类型时， &表示按位与操作，
         */
        return IsBalanced_Solution(root.left) & IsBalanced_Solution(root.right);
    }

    public int getTreeDepth(TreeNode root) {
        if (null == root) {
            return 0;
        }
        int leftDepth = getTreeDepth(root.left) + 1;
        int rightDepth = getTreeDepth(root.right) + 1;
        return leftDepth > rightDepth ? leftDepth : rightDepth;
    }
}
