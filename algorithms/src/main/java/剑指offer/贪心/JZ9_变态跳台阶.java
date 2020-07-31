package 剑指offer.贪心;

/**
 * 题目描述
 * 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
 *
 * @author: kfzx-menghj
 * @Time: 2020/7/31  12:26
 */
public class JZ9_变态跳台阶 {
    public int JumpFloorII(int target) {
        /**
         * 关于本题，前提是n个台阶会有一次n阶的跳法。分析如下:
         *
         * f(1) = 1
         * f(2) = f(2-1) + f(2-2)         //f(2-2) 表示2阶一次跳2阶的次数。
         * f(3) = f(3-1) + f(3-2) + f(3-3)
         * 得出最终结论,在n阶台阶，一次有1、2、...n阶的跳的方式时，总得跳法为：
         *        | 1       ,(n=0 )
         * f(n) = | 1       ,(n=1 )
         *        | 2*f(n-1),(n>=2)
         */
        int count = 0;
        if (target <= 1) {
            return 1;
        }
        for (int i = 1; i <= target; i++) {
            count = count + JumpFloorII(target - i);
        }
        return count;
    }
}
