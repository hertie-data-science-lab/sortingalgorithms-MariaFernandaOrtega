from bucket_radix import bucketSort

import random
import time



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
