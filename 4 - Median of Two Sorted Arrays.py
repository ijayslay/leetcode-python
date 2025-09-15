# 4 - Median of Two Sorted Arrays
# Difficulty: Hard
# Tags: Array, Binary Search, Divide and Conquer

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Finds the median of two sorted arrays using a binary search approach.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to optimize the binary search range.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        half_len = (m + n + 1) // 2

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = half_len - partitionX

            # Use float('-inf') and float('inf') for compatibility.
            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX != m else float('inf')

            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY != n else float('inf')
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    max_of_left = max(maxLeftX, maxLeftY)
                    min_of_right = min(minRightX, minRightY)
                    return (max_of_left + min_of_right) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1