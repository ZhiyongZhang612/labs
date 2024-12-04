def zipmap(key_list, value_list, override=False):
    adjusted_values = (
        value_list[:len(key_list)] if len(value_list) > len(key_list)
        else value_list + [None] * (len(key_list) - len(value_list))
    )

    pairs = zip(key_list, adjusted_values)

    if override:
        return dict(pairs)
    else:
        unique_keys = set()
        return dict(filter(
            lambda kv: kv[0] not in unique_keys and not unique_keys.add(kv[0]),
            pairs
        ))

if __name__ == "__main__":
    print(zipmap(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5, 6]))

    print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))

    print(zipmap([1, 2, 3], [4, 5, 6, 7, 8]))

    print(zipmap([1, 3, 5, 7], [2, 4, 6]))
