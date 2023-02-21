import time


def findMedianSortedArrays(nums1, nums2):
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

        print((num[n - 1] + num[n]) / 2)
    else:
        print(num[n])


class Solution:

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


if __name__ == '__main__':
    # 中间数
    a = [1, 2]
    b = [3, 4, 8, 1]
    # a.extend(b)
    # a.sort()
    output = findMedianSortedArrays(a, b)
    print(output)

    # 最长回文数
    s = "ccd"
    print(Solution().longestPalindrome(s))
