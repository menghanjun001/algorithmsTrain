package 剑指offer.数学运算;


/**
 * 题目描述
 * 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
 *
 * @author: kfzx-menghj
 * @Time: 2020/7/31  11:29
 */
public class JZ48_不用加减乘除做加法 {
    public int Add(int num1, int num2) {
        /**
         * 异或的结果和相加一致
         * 1^1=0 1^0=1 0^0=1
         */
        int var1 = num1 ^ num2;
        /**
         * 与的结果和进位一致
         * 1&1=1 1&0=0 0&0=0
         */
        int var2 = (num1 & num2) << 1;
        return var1 + var2;
    }
}
