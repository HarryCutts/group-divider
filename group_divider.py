#!/usr/bin/env python3
from collections import namedtuple
import random

GroupMember = namedtuple('GroupMember', ['name', 'size'])

def parse_member(line):
    return GroupMember(line.strip(), len(line.split('&')))

def divide_by_sizes(members, group_sizes):
    free_space = list(group_sizes)
    groups = [[] for i in range(len(free_space))]
    remaining = []

    for member in members:
        assigned = False
        for i, group in enumerate(groups):
            if free_space[i] >= member.size:
                assigned = True
                group.append(member)
                free_space[i] -= member.size;
                break

        if not assigned:
            remaining.append(member)

    if remaining:
        print("Warning:", len(remaining), "were left out:", ", ".join(m.name for m in remaining))

    return groups

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Divides a list into random groups")
    parser.add_argument('names_file', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help="A file containing the names to assign")
    parser.add_argument('--group-sizes', type=str, help="A comma-separated list of the sizes of groups to create")
    args = parser.parse_args()

    with args.names_file:
        members = map(parse_member, args.names_file.readlines())

    shuffled_members = [*members]
    random.shuffle(shuffled_members)

    group_sizes = map(int, args.group_sizes.split(','))
    groups = divide_by_sizes(shuffled_members, group_sizes)

    for i, group in enumerate(groups):
        print("Group {}: {}".format(i, ", ".join(m.name for m in group)))
