def is_set(data):
    if data is None:
        return False
    new_set = []
    for num in data:
        if num in new_set:
            return False
        new_set.append(num)
    return True

test_cases = [[1, 2, 3, 4, 5],[5, 5],[],None]
results = [is_set(case) for case in test_cases]
print(results)