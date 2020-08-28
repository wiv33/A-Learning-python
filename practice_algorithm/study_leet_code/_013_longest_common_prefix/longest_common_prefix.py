# https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs or not strs[0]:
            return ""

        sort_data = sorted(strs, key=len)
        word_size = len(sort_data[0])
        common_prefix = sort_data[0]
        while word_size > 0:
            got_it = common_prefix[:word_size]
            for word in sort_data:
                if not word.startswith(common_prefix[:word_size]):
                    got_it = ""
                    break

            if got_it:
                return got_it

            word_size -= 1

        return ""

    def longestCommonPrefix_2(self, strs: [str]) -> str:
        common_prefix, word_size = strs[0], len(strs[0])
        while word_size > 0:
            got_it = common_prefix[:word_size]
            for word in strs[1:]:
                if not word.startswith(common_prefix[:word_size]):
                    got_it = ""
                    break

            if got_it:
                return got_it

            word_size -= 1

        return ""
