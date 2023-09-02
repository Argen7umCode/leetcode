def merge(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] +  nums2[:n])


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3

merge(nums1, m, nums2, n)
assert nums1 == [1,2,2,3,5,6]


nums1 = [1]
nums2 = []

m = 1
n = 0

merge(nums1, m, nums2, n)
assert nums1 == [1]


nums1 = [0]
nums2 = [1]

m = 0
n = 1

merge(nums1, m, nums2, n)
assert nums1 == [1]