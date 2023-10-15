def bubble(nums):
    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__":
    #numbers = range(100, 0, -1)
    #nums = list(numbers)
    nums = [8, 8, 8, 8, 4, 8, 8, 1]
    result = bubble(nums)
    print(result)
