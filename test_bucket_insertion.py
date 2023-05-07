from bucket_insertion import bucketSort

# Testing bucketSort algorithm (insertion sort)

import random
import time

# Generating random input array
random.seed(1)
array = [random.randint(0, 99) for _ in range(10000)]

# Print unsorted array
print("Unsorted array: ", array)

start_time = time.time()
# Sort the array using bucketSort
array = bucketSort(array)
end_time = time.time()

# Print sorted array
print("Sorted array: ", array)

print("Time taken: ", end_time - start_time)
