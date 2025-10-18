/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
#include <climits>
#include <vector>
class Solution {
public:
    // int maxProfit(std::vector<int> &prices) {
    //     int length = prices.size();
    //     std::vector<std::vector<std::tuple<int, int>>> dp(length, std::vector<std::tuple<int, int>>(length));
    //     // (length, length), each element storing the (int, int)

    //     // initialize
    //     for (int i = 0; i < length; i++) {
    //         dp[i][i] = {prices[i], prices[i]};
    //     }

    //     for (int i = 1; i < length; i++) {
    //         for (int j = 0; i + j < length; j++) {
    //             if()
    //         }
    //     }
    // }
    // int maxProfit(std::vector<int> &prices) {
    //     int length = prices.size();
    //     std::vector<std::vector<int>> dp(length, std::vector<int>(2));
    //     // initialize
    //     dp[0][0] = 0;
    //     dp[0][1] = -prices[0];

    //     for (int i = 1; i < length; i++) {
    //         dp[i][1] = std::max(dp[i - 1][1], -prices[i]);
    //         dp[i][0] = std::max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
    //     }

    //     return dp[length - 1][0];
    // }

    int maxProfit(std::vector<int> &prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            // 更新最低价格
            minPrice = std::min(minPrice, price);

            // 更新最大利润
            maxProfit = std::max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
};
// @lc code=end
