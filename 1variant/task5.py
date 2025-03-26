def f(x):
    nums = [int(num) for num in str(x)]
    x1 = nums[0] + nums[2] + nums[4]
    x2 = nums[1] + nums[3]
    sorted_sums = sorted([x1, x2], reverse=True)[:2]
    return int(str(sorted_sums[1]) + str(sorted_sums[0]))

min_number = []

for i in range(10000, 100000):
    if f(i) == 723:
        min_number.append(i)


print(min(min_number))