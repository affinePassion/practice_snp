def coincidence(list = [], range = range):
    result_array = []
    for i in list:
        if isinstance(i, (int, float)) and range.start <= i < range.stop:
            result_array.append(i)
            
    return result_array

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))