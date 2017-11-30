#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    if capacity*len(items) < 125000000:
        return simple_dynamic_programming_solution(items, capacity)
    return greedy_solution(items, capacity)

def greedy_solution(items, capacity):
    value = 0
    weight = 0
    taken = [0] * len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def simple_dynamic_programming_solution(items, capacity):
    items_length = len(items)
    dp = [[0 for item in range(items_length+1)] for k in range(capacity+1)]

    for k in range(1, capacity+1):
        for idx, item in enumerate(items):
            if item.weight > k:
                dp[k][idx+1] = dp[k][idx]
            else:
                dp[k][idx+1] = max(
                    dp[k-item.weight][idx] + item.value,
                    dp[k][idx])

    max_value = dp[k][idx+1]
    # backtrack to retrieve output
    output = []
    curr_idx = items_length-1
    current_capacity = capacity

    for idx in range(items_length, 0, -1):
        if dp[current_capacity][idx] == \
                dp[current_capacity][idx - 1]:  # we didn't choose that item
            output.append(0)
        else:
            current_capacity = current_capacity - items[idx-1].weight
            output.append(1)

    output_reversed = output[::-1]

    output_data = str(max_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, output_reversed))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

