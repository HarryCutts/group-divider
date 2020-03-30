#!/usr/bin/env python3
import random

def divide(shuffled_names, num_groups):
    group_size = len(names) // num_groups
    groups = []
    for i in range(0, len(names), group_size):
        groups.append(shuffled_names[i:i+group_size])
    if len(groups[-1]) < group_size:
        groups[-2].extend(groups[-1])
        del groups[-1]

    return groups

def divide_by_sizes(shuffled_names, group_sizes):
    groups = []
    i = 0
    for size in group_sizes:
        groups.append(shuffled_names[i:i+size])
        i += size

    if i != len(shuffled_names):
        remaining = shuffled_names[i:]
        print("Warning:", len(remaining), "were left out:", ", ".join(remaining))

    return groups

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Divides a list into random groups")
    parser.add_argument('names_file', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help="A file containing the names to assign")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--num-groups', type=int, help="The number of groups to create")
    group.add_argument('--group-sizes', type=str, help="A comma-separated list of the sizes of groups to create")
    args = parser.parse_args()

    with args.names_file:
        names = list(map(str.strip, args.names_file.readlines()))

    shuffled_names = [*names]
    random.shuffle(shuffled_names)

    if args.num_groups is not None:
        groups = divide(shuffled_names, args.num_groups)
    else:
        group_sizes = map(int, args.group_sizes.split(','))
        groups = divide_by_sizes(shuffled_names, group_sizes)

    for i, group in enumerate(groups):
        print("Group {}: {}".format(i, ", ".join(group)))
