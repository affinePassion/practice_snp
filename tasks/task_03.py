def max_odd(array = None):
    result_max = 0
    for i in array:
        if isinstance(i, (int, float)):
            if i % 2 != 0 and i > result_max:
                result_max = i

    return int(result_max) if result_max != 0 else None

print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))