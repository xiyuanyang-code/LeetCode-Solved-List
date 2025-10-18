/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        // std::vector<int> dp(n, 0);

        // // initial settings
        // dp[0] = 1;
        // dp[1] = 2;
        // for (int i = 2; i < n; i++) {
        //     dp[i] = dp[i - 1] + dp[i - 2];
        // }

        int before, after;
        int tmp = 0;
        before = 2;
        after = 1;
        for (int i = 2; i < n; i++) {
            tmp = after;
            after = before;
            before = tmp + after;
        }

        return before;
        // return dp[n - 1];
    }
};
// @lc code=end
