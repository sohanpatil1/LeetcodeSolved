def rob(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    tracker = [0] * len(nums)
    tracker[0] = nums[0]
    tracker[1] = max(nums[0], nums[1])  #Important mistake. You could take either value
    for i in range(2, len(nums)):
        maxval = max(nums[i]+tracker[i-2], tracker[i-1])
        tracker[i] = maxval
    return tracker[-1]


nums = [2, 1, 1, 2]
result = rob(nums)
print(result)