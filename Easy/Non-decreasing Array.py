def checkPossibility(nums):
    index = -1
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            if index != -1:
                return False
            index = i
    if index == -1 or index == 0 or index == len(nums)-2 or nums[index-1] <= nums[index+1] or nums[index] <= nums[index+2]:
        return True
    return False

print(checkPossibility([4,2,3]))
print(checkPossibility([4,2,1]))
print(checkPossibility([3,4,2,4]))
print(checkPossibility([1,5,4,6,7,10,8,9]))
                