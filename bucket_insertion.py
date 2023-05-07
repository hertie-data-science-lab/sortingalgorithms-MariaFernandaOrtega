# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:52:46 2023

@author: Hannah
"""

from insertion import insertionSort

def bucketSort(array):
    if len(array) == 0:
        return array

    # Empty buckets
    bucket = [[] for _ in range(len(array))]

    # Inserting elements into their respective buckets
    for j in array:
        index_b = int(0.1 * j)
        bucket[index_b].append(j)

    # Sorting the elements of each bucket using sorting algorithm (insertion sort)
    for i in range(len(array)):
        bucket[i] = stableSort(bucket[i])

    # Merge sorted buckets
    return [elem for bucket_list in bucket for elem in bucket_list]


def stableSort(array):
    if len(array) <= 1:
        return array

    # choosing stable sorting algorithm (insertion sort)
    sorted_array = insertionSort(array)

    return sorted_array


