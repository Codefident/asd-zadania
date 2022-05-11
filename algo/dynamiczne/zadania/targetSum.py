# target sum

nums = [1]
target = 1


def plus(nums, i, n):
    s = n + nums[i]

    if i == 0:
        if s == 0:
            return 1
        else:
            return 0
    return plus(nums, i-1, s) + minus(nums, i-1, s)


def minus(nums, i, n):
    s = n - nums[i]

    if i == 0:
        if s == 0:
            return 1
        else:
            return 0
    return plus(nums, i-1, s) + minus(nums, i-1, s)


def targetSum(nums, target):
    return plus(nums, len(nums) - 1, target) + minus(nums, len(nums) - 1, target)

print(targetSum(nums, target))