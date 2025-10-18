/*
 * @lc app=leetcode id=72 lang=cpp
 *
 * [72] Edit Distance
 */

// @lc code=start
#include <cmath>
#include <string>
#include <vector>
class Solution {
public:
    int minDistance(std::string word1, std::string word2) {
        int word_length_1 = word1.length();
        int word_length_2 = word2.length();

        std::vector<std::vector<int>> dp(word_length_1 + 1, std::vector<int>(word_length_2 + 1));

        // initialize
        for (int i = 0; i <= word_length_1; i++) {
            dp[i][0] = i;
        }

        for (int j = 0; j <= word_length_2; j++) {
            dp[0][j] = j;
        }

        if (word_length_1 == 0 && word_length_2 == 0) {
            return dp[word_length_1][word_length_2];
        }


        // start dp!
        for (int i = 1; i <= word_length_1; i++) {
            for (int j = 1; j <= word_length_2; j++) {

                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + std::min(dp[i - 1][j], std::min(dp[i][j - 1], dp[i - 1][j - 1]));
                }
            }
        }

        return dp[word_length_1][word_length_2];
    }
};
// @lc code=end
