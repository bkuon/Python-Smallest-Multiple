def lowest_common_multiple(a, b):

    return a * b / highest_common_multiple(a, b)


def highest_common_multiple(a, b):

    if b == 0:
        return a
    else:
        return highest_common_multiple(b, (a % b))


result = 1
for i in range(2, 20):
    result = lowest_common_multiple(i, result);

print(result)
