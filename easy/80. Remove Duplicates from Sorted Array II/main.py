from collections import Counter

def removeDuplicates(nums):
    d = dict()
    indexes = []
    for i, num in enumerate(nums):
        try:
            d[num] += 1
        except:
            d[num] = 1
        print(nums)
        if d[num] > 2:
            indexes.append(i-1)
    for i in indexes[::-1]:
        del nums[i]
    return len(nums)

def test(nums, out):
    assert removeDuplicates(nums) == out[1] and nums == out[0]

nums = [0] * 5
# test(nums, ([1,1,2,2,3], 5))
print(removeDuplicates(nums))
print(nums)