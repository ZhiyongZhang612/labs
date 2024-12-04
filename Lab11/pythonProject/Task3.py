from functools import reduce

def filter_with_reduce(f, target_list):
    return reduce(
        lambda acc, x: acc + [x] if f(x) else acc,
        target_list,
        []
    )

