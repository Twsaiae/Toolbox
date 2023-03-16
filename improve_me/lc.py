import time


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
    算法的时间复杂度应该为 O(log (m+n)) 。

        输入：nums1 = [1,3], nums2 = [2]
        输出：2.00000
        解释：合并数组 = [1,2,3] ，中位数 2

        输入：nums1 = [1,2], nums2 = [3,4]
        输出：2.50000
        解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -106 <= nums1[i], nums2[i] <= 106


        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = [1, 2]
        nums2 = [3, 4]
        total_length = len(nums1) + len(nums2)
        n = int(total_length / 2)
        idx1 = 0
        idx2 = 0
        num = []
        for i in range(n + 1):
            # print(idx1, idx2, num)

            if idx1 >= len(nums1):
                num.append(nums2[idx2])
                idx2 += 1
                continue
            if idx2 >= len(nums2):
                num.append(nums1[idx1])
                idx1 += 1
                continue
            if nums1[idx1] <= nums2[idx2]:
                num.append(nums1[idx1])
                idx1 += 1
            else:
                num.append(nums2[idx2])
                idx2 += 1
        # print(num)
        # print(n)
        if total_length % 2 == 0:

            return (num[n - 1] + num[n]) / 2
        else:
            return num[n]

    def longestPalindrome(self, s: str) -> str:
        """
        动态规划
        给你一个字符串 s，找到 s 中最长的回文子串。

        如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
        :param s:str
        :return:str

        一天后再理思绪：
            1、问题拆解：把寻找最长回文数拆解成判断是回文数+寻找最长
            2、寻找最长最好的方法就是过一遍的方法
            怎么一遍过呢?
            再拆分可能的情况：拆分成奇数情况+偶数情况+特殊情况
            特殊情况特殊处理，然后想办法把奇数和偶数一次过了
            咱们只会从头遍历，先把必须要进行的路走了，再往后考虑
            """
        if len(s) < 2 or s == s[::-1]:
            return s

        l_p = s[0]
        max_len = 1

        for i in range(1, len(s)):
            odd = s[i - max_len - 1: i + 1]
            even = s[i - max_len:i + 1]

            if even == even[::-1] and len(even) > max_len:
                l_p = even
                max_len += 1
                continue
            if odd == odd[::-1] and len(odd) > max_len:
                l_p = odd
                max_len += 2
                continue
        return l_p

    def minimumDeletions(self, s: str) -> int:
        """
        属于枚举法，思考最终结果的可能性，全是a、全是b，左边是a右边是b。
        如何达到这些情况呢，全是a就是删除所有b，全是b就是删除所有a，左a右b的话就是找个中间位置，然后把左边的b全部删除，右边的a全部删除

        """
        leftb, righta = 0, s.count('a')
        res = righta
        for c in s:
            if c == 'a':
                righta -= 1
            else:
                leftb += 1
            res = min(res, leftb + righta)
        return res

    def convert(self, s: str, numRows: int) -> str:
        """
        我想的是把规律整理起来然后用自己的方式来写入
        人家使用代码来描述N字变换的过程，并在这个过程中去

        """
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

    def isMatch(self, s: str, p: str) -> bool:
        """
        给你一个字符串 s 和一个字符规律 p，请你来实现一个支持
        '.' 和 '*' 的正则表达式匹配。

        '.'
        匹配任意单个字符
        '*'
        匹配零个或多个前面的那一个元素
        所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 初始化
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # 状态更新
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':  # 【题目保证'*'号不会是第一个字符，所以此处有j>=2】
                    if s[i - 1] != p[j - 2] and p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2] | dp[i - 1][j]

        return dp[m][n]



        # idx1 = 0
        # idx2 = 0
        # l_s = len(s)
        # l_p = len(p)
        # # 1.一种是消不了直接报错
        # for idx2 in range(l_p):
        #     if idx1 == l_s:
        #         if p[idx2] == '*' and idx2 == l_p - 1:
        #             return True
        #         else:
        #             return False
        #     if p[idx2] == '*':
        #         continue
        #     # 1.1一种是单个字母或.+*
        #     if idx2 < l_p - 1 and p[idx2 + 1] == '*':
        #         # 那么就进行第二类判断,这个有分成 字母+*匹配到/字母+*匹配不到/.加*
        #         if p[idx2] == '.':
        #             if idx2 + 2 == l_p:
        #                 return True
        #             else:
        #                 return False
        #
        #         elif p[idx2] == s[idx1]:
        #             for idx in range(idx1, l_s):
        #                 if s[idx] != p[idx2]:
        #                     break
        #                 idx1 += 1
        #         else:
        #             continue
        #     # 1.2 单个字母或.
        #     else:
        #         if p[idx2] == s[idx1] or p[idx2] == '.':
        #             idx1 += 1
        #         else:
        #             return False
        # # 2.一种是可以一直消完，但是s没消完
        # if idx1 > l_s - 1:
        #     return True
        # else:
        #     return False


if __name__ == '__main__':
    # # 中间数
    # a = [1, 2]
    # b = [3, 4, 8, 1]
    # output = findMedianSortedArrays(a, b)
    # print(output)

    # # 最长回文数
    # s = "ccd"
    # print(Solution().longestPalindrome(s))

    # # 最少删除次数
    # s = "baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb"
    # print(Solution().minimumDeletions(s))

    # # N字变换
    # s = "PAYPALISHIRING"
    # print(Solution().convert(s,3))

    # 正则表达式      跟上一道题一样，我的思路是用代码描述规则即可
    s = 'aaaabacccc'
    p = 'a*ab.*'

    print(Solution().isMatch(s, p))

