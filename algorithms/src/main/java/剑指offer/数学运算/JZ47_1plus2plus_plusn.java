package 剑指offer.数学运算;

/**
 * 题目描述
 * 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
 *
 * @author: kfzx-menghj
 * @Time: 2020/7/31  13:07
 */
public class JZ47_1plus2plus_plusn {
    public int Sum_Solution(int n) {
        /**
         * 需利用逻辑与的短路特性实现递归终止
         */
        boolean var0 = (n >= 1) && ((n+=Sum_Solution(n - 1))>0);
//        可以变形为
//        if ((n >= 1)) {
//            n += Sum_Solution(n - 1);
//        }
        return n;
    }

}
