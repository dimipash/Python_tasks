class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge sorted arrays nums1 and nums2 in-place.

        Args:
        nums1 (List[int]): Array with extra space at end, modified in-place.
        m (int): Number of elements in nums1.
        nums2 (List[int]): Array to be merged into nums1.
        n (int): Number of elements in nums2.
        """

        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()
