package 剑指offer.递归;

/**
 * 题目描述
 * 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
 * @author: kfzx-menghj
 * @Time: 2020/7/31  16:11
 */
public class JZ8_跳台阶 {
    public int JumpFloor(int target) {
        if (target <= 1) {
            return 1;
        }
        return JumpFloor(target - 1) + JumpFloor(target - 2);
    }

    /**
     * 链接：https://www.nowcoder.com/questionTerminal/8c82a5b80378478f9484d87d1c5f12a4?answerType=1&f=discussion
     * 来源：牛客网
     *
     * 方法一：递归
     * 题目分析，假设f[i]表示在第i个台阶上可能的方法数。逆向思维。如果我从第n个台阶进行下台阶，下一步有2中可能，一种走到第n-1个台阶，一种是走到第n-2个台阶。所以f[n] = f[n-1] + f[n-2].
     * 那么初始条件了，f[0] = f[1] = 1。
     * 所以就变成了：f[n] = f[n-1] + f[n-2], 初始值f[0]=1, f[1]=1，目标求f[n]
     * 看到公式很亲切，代码秒秒钟写完。
     *
     * int Fibonacci(int n) {
     *     if (n<=1) return 1;
     *     return Fibonacci(n-1) + Fibonacci(n-2);
     * }
     * 优点，代码简单好写，缺点：慢，会超时
     * 时间复杂度：O(2^n)
     * 空间复杂度：递归栈的空间
     * ###方法二：记忆化搜索
     * 拿求f[5] 举例
     *
     *
     * 通过图会发现，方法一中，存在很多重复计算，因为为了改进，就把计算过的保存下来。
     * 那么用什么保存呢？一般会想到map， 但是此处不用牛刀，此处用数组就好了。
     *
     * int Fib(int n, vector<int>& dp) {
     *     if (n<=1) return 1;
     *     if (dp[n] != -1) return dp[n];
     *     return dp[n] = Fib(n-1) + Fib(n-2);
     * }
     * int Fibonacci(int n) {
     *     vector<int> dp(45, -1); // 因为答案都是>=0 的， 所以初始为-1，表示没计算过
     *     return Fib(n, dp);
     * }
     * 时间复杂度：O（n）， 没有重复的计算
     * 空间复杂度：O（n）和递归栈的空间
     *
     * 方法三：动态规划
     * 虽然方法二可以解决此题了，但是如果想让空间继续优化，那就用动态规划，优化掉递归栈空间。
     * 方法二是从上往下递归的然后再从下往上回溯的，最后回溯的时候来合并子树从而求得答案。
     * 那么动态规划不同的是，不用递归的过程，直接从子树求得答案。过程是从下往上。
     *
     * int Fibonacci(int n) {
     *     vector<int> dp(n+1, 0);
     *         dp[0] = dp[1] = 1;
     *         for (int i=2; i<=n; ++i) {
     *             dp[i] = dp[i-1] + dp[i-2];
     *         }
     *         return dp[n];
     * }
     * 时间复杂度：O(n)
     * 空间复杂度：O(n)
     */
}
