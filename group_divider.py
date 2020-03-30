#!/usr/bin/env python3
from collections import namedtuple
import random
import sys

GroupMember = namedtuple('GroupMember', ['name', 'size'])

def parse_member(line):
    return GroupMember(line.strip(), len(line.split('&')))

def divide_by_sizes(members, group_sizes, leaders):
    free_space = list(group_sizes)
    groups = [[] for i in range(len(free_space))]
    remaining = []

    if leaders:
        if len(leaders) > len(free_space):
            fatal("Too many leaders to put into individual groups.", file=sys.stderr)
            exit()

        for i, leader in enumerate(leaders):
            groups[i].append(leader)
            free_space[i] -= leader.size
            if free_space[i] <= 0:
                print("Warning: group", i, "is already full after leader assignment.", file=sys.stderr)

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

    parser = argparse.ArgumentParser(
            description="Divides a list of names into random groups",
            epilog="In names files, names of inseparable people can be put on the same line, joined with an ampersand (&).")
    parser.add_argument('names_file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
            help="A file containing the names to assign (defaults to standard input)")
    parser.add_argument('leaders_file', type=argparse.FileType('r'), nargs='?', default=None,
            help="A file containing the names of leaders, who will be assigned to groups in order")
    parser.add_argument('--group-sizes', type=str,
            help="A comma-separated list of the sizes of groups to create")
    args = parser.parse_args()

    if args.leaders_file:
        with args.leaders_file:
            leaders = list(map(parse_member, args.leaders_file.readlines()))
    else:
        leaders = None

    with args.names_file:
        members = map(parse_member, args.names_file.readlines())

    shuffled_members = [*members]
    random.shuffle(shuffled_members)

    group_sizes = map(int, args.group_sizes.split(','))
    groups = divide_by_sizes(shuffled_members, group_sizes, leaders)

    for i, group in enumerate(groups):
        print("Group {}: {}".format(i, ", ".join(m.name for m in group)))
