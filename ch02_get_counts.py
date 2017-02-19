# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:17:38 2017

@author: Administrator
"""

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] = counts[x] + 1
        else:
            counts[x] = 1
    return counts



from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
