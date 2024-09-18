def make_set(data):
    new_data = []
    for num in data:
        if num not in new_data:
            new_data.append(num)
    return new_data

test_data = {1, 2, 3, 4, 4, 5}
result=make_set(test_data)
print(result)