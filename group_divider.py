#!/usr/bin/env python3
import random

def divide(names, num_groups):
    shuffled_names = [*names]
    random.shuffle(shuffled_names)
    group_size = len(names) // num_groups
    groups = []
    for i in range(0, len(names), group_size):
        groups.append(shuffled_names[i:i+group_size])
    if len(groups[-1]) < group_size:
        groups[-2].extend(groups[-1])
        del groups[-1]

    return groups

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Divides a list into random groups")
    parser.add_argument('--num-groups', type=int, help="The number of groups to create")
    parser.add_argument('names_file', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help="A file containing the names to assign")
    args = parser.parse_args()

    with args.names_file:
        names = list(map(str.strip, args.names_file.readlines()))

    groups = divide(names, args.num_groups)

    for i, group in enumerate(groups):
        print("Group {}: {}".format(i, ", ".join(group)))
