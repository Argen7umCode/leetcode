def removeDuplicates(nums) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)


print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))