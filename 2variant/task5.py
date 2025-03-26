def f(x):
    nums = [int(num) for num in str(x)]
    x1 = int(nums[0]) + int(nums[1])
    x2 = int(nums[1]) + int(nums[2])
    x3 = int(nums[2]) + int(nums[3])
    sorted_sums = sorted([x1, x2, x3], reverse=True)[:2]
    return int(str(sorted_sums[1]) + str(sorted_sums[0]))

numbers = []

for i in range(1000, 10000):
    if f(i) == 1418:
        numbers.append(i)


print(min(numbers))