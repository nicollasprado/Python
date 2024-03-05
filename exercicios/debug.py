def twoSum(nums, target):
    findIndexStartValue = 0
    for val1 in nums:
        findIndexStartValue += 1
        for val2 in nums[findIndexStartValue:]:
            add_numbers = val1 + val2
            if add_numbers == target:
                return nums.index(val1), nums.index(val2, findIndexStartValue)
            else:
                continue
print(twoSum([2, 5, 5, 11], 10))



def isPalindrome(x: int) -> bool:
    invertedNumber = ''
    numberStr = str(x)
    numberList = list(numberStr)
    print(numberList)
    aa = numberList.reverse()
    print(aa)
    for number in numberList:
        invertedNumber = number + invertedNumber
    if invertedNumber == numberStr:
        return True
    else:
        return False
    

print(isPalindrome(121))


# z = '2198'
# y = z[::-1]
# print(y)