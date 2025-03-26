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
        nums = [int(num) for num in str(decimal_number)]
        sum_nums = sum(nums)
    return int(x, 2)


lower_bound = 987654321
upper_bound = 2123456789
count = 0
max_n = 10000000
progress_step = max_n // 100

print("Processing: ", end="", flush=True)
n = 1
while True:
    R = f(n)
    if R > upper_bound:
        break
    if lower_bound <= R <= upper_bound:
        count += 1

    if n % progress_step == 0:
        progress_percent = (n // progress_step)
        print(f"\rProcessing: {progress_percent}%", end="", flush=True)

    n += 1

print("\nProcessing: 100%")
print("\nDone!")
print(f"Count: {count}")