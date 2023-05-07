[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Trv1ybv1)
# Sorting Algorithms

## Team members:
Maria Jose Lee
Maria Fernanda Ortega

## Code Explanation 
This project contains four tabs:
- bucket_insertion: bucket algorithm sorted by Insertion algorithm
- test_bucket_insertion: testing the algorithm bucket_insertion
- bucket_radix:  bucket algorithm sorted by Radix algorithm
- test_bucket_radix: testing the algorithm bucket_radix

## Time complexity 
- Insertion Sort: O(n^2)
-Radix Sort: O(d(n+k)), where d is the number of digits in the maximum number and k is the radix (for example, k=10 for decimal numbers)

When timing both algorithms in this project we confirm that Radix Sort is more time efficient 

## Assignment:

A Bucket sort can use any stable sorting algorithm to sort the elements in its buckets.
It can also recursively sort the elements in its buckets into smaller buckets. This is useful when the buckets are still large and unsorted after the first pass of a bucket sort.
Rewrite the bucket sort algorithm to call itself until each bucket contains only one element or is already sorted by another algorithm (you may use any stable sorting algorithm).

* You may use the code provided in this repository as a starting point.
* You may choose to edit bucket.py or copy the contents into a new file. either way, let me know which is your final submission.
* [Document](https://realpython.com/documenting-python-code/) your code and use [modular programming](https://realpython.com/python-modules-packages/#executing-a-module-as-a-script) to maximise the quality of your code.


## Additional Notes

* Please do not double-submit. If you are part of a group, do not submit a separate assignment as well.
* List your group members in the README file or in the header for your submission.
* Submit by May 8 at 12 am.
