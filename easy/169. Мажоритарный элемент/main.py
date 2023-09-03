def rotate(nums, k) -> None:
    k = k % len(nums) if k > len(nums) else k
    nums[:] = (nums[:-k][::-1] + nums[-k:][::-1])[::-1]


rotate([1,2,3,4,5,6,7], 3)
print()
rotate([-1,-100,3,99], 2)


