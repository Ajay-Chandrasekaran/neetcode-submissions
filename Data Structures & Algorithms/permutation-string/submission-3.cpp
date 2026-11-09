class Solution {
public:
    bool checkInclusion(const std::string& s1, const std::string& s2) {
        const size_t n = s1.size(), m = s2.size();
        if (n > m) return false;

        // diff[c] = count in s1 - count in current window of s2
        std::array<int, 26> diff{};
        for (size_t i = 0; i < n; ++i) {
            ++diff[s1[i] - 'a'];
            --diff[s2[i] - 'a'];
        }

        constexpr std::array<int, 26> zero{};
        for (size_t r = n; r < m; ++r) {
            if (diff == zero) return true;
            --diff[s2[r] - 'a'];      // incoming
            ++diff[s2[r - n] - 'a'];  // outgoing
        }

        return diff == zero;
    }
};