def intersection(setA, setB):
    if not isinstance(setA, list) or not isinstance(setB, list):
        return []
    if len(setA) != len(set(setA)) or len(setB) != len(set(setB)):
        return []
    result = []

    for element in setA:
        if element in setB:
            result.append(element)

    return result
print(intersection([1, 2], [2, 3]))
print(intersection([], [2, 3]))
print(intersection([1, 1, 1], [2]))

