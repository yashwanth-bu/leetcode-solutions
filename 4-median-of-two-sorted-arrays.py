class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        combine_nums = nums1 + nums2
        sorted_nums = sorted(combine_nums)
        length_nums = len(sorted_nums)

        if length_nums % 2 == 0:
            index = length_nums // 2
            return (sorted_nums[index - 1] + sorted_nums[index]) / 2.0
        else:
            index = length_nums // 2
            return float(sorted_nums[index])
