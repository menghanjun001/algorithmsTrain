package 剑指offer;


import org.junit.Test;
import 剑指offer.POJO.TreeNode;
import 剑指offer.树.JZ38_二叉树的深度;

public class JZ38_二叉树的深度Test {

    @Test
    public void treeDepth() {
        TreeNode treeNode = new TreeNode(3);
        treeNode.left = new TreeNode(2);
        treeNode.left.left = new TreeNode(1);

        JZ38_二叉树的深度 var = new JZ38_二叉树的深度();
        System.out.println(var.TreeDepth(treeNode));
    }
}