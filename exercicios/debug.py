def twoSum(nums, target):
    for val1 in nums:
        for val2 in nums:
            add_numbers = val1 + val2
            if add_numbers == target:
                return nums.index(val1), nums.index(val2)
            else:
                continue
print(twoSum([3,3], 6))