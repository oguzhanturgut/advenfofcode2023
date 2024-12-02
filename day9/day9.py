# Part 1
# def f(nums):
#     if all(x == 0 for x in nums):
#         return 0
#     temp = []
#     for i in range(len(nums) - 1):
#         temp.append(nums[i + 1] - nums[i])
#     return nums[-1] + f(temp)
#
#
# with open('day9.txt') as file:
#     lines = file.readlines()
#     ans = 0
#     for line in lines:
#         xs = [int(x) for x in line.strip().split()]
#         ans += f(xs)
#     print(ans)


# Part 2
def f(nums):
    if all(x == 0 for x in nums):
        return 0
    temp = []
    for i in range(len(nums) - 1):
        temp.append(nums[i + 1] - nums[i])
    return nums[0] - f(temp)


with open('day9.txt') as file:
    lines = file.readlines()
    ans = 0
    for line in lines:
        xs = [int(x) for x in line.strip().split()]
        ans += f(xs)
    print(ans)


