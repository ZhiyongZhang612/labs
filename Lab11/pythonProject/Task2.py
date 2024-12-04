from collections import defaultdict


def group_by(f, target_list):
    grouped = defaultdict(list)

    list(map(lambda x: grouped[f(x)].append(x), target_list))

    return dict(grouped)


if __name__ == "__main__":
    print(group_by(len, ["hi", "dog", "me", "bad", "good"]))