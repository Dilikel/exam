#56533
def f(n):
    nums = [int(num) for num in str(n)]
    sum_nums = sum(nums)
    x = bin(n)[2:]
    for i in range(3):
        if sum_nums % 2 == 0:
            x += '0'
        else:
            x += '1'
        decimal_number = int(x, 2)
        nums = [int(digit) for digit in str(decimal_number)]
        sum_nums = sum(nums)
    return int(x, 2)

print(f(17))