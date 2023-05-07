def bucketSort(array):
    if len(array) == 0:
        return array

    # Creating empty buckets
    bucket = [[] for _ in range(len(array))]

    # Inserting elements into their respective buckets
    for j in array:
        index_b = int(0.1 * j)
        bucket[index_b].append(j)

    # Sorting the elements of each bucket using radix sort
    for i in range(len(array)):
        radixSort(bucket[i])

    # Merging sorted buckets
    return [elem for bucket_list in bucket for elem in bucket_list]


def radixSort(array):
    if len(array) == 0:
        return array

    # Getting maximum element
    max_element = max(array)

    # Applying counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

    return array


def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculating cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Placing the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]



