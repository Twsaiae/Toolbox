class Solution(object):
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
            print(idx1, idx2, num)

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
        print(num)
        print(n)
        if total_length % 2 == 0:

            print((num[n - 1] + num[n]) / 2)
        else:
            print(num[n])


if __name__ == '__main__':


