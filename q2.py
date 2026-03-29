
def find_median(numbers):
    if not numbers:
        return None

    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    median = n // 2


    if n % 2 == 1:
        median = numbers_sorted[median]
    else:
        median = (numbers_sorted[median - 1] + numbers_sorted[median]) / 2

    return median

print(float(find_median([3, 1, 4, 1, 5])))
print(float(find_median([7, 2, 10, 9])))
print(float(find_median([42])))