def union(setA,setB):
    if not isinstance(setA, list) or not isinstance(setB, list):
        return []
    if len(setA) != len(set(setA)) or len(setB) != len(set(setB)):
        return []
    result=[]
    for element in setA:
        if element not in result:
            result.append(element)
    for num in setB:
        if num not in setA:
            result.append(num)
    return result

print(union([1,2],[2,3]))
print(union([],[2,3]))
print(union([1,1,1],[2,3]))