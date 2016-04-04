import random
import copy

#######################   Merge Sort   #######################

def merge_sort(source, start_index, end_index, target):
    """
    Parameter Type: 
        source:
            The list of objects that can be compared with operartor < <= == >= >
        startIndex & endIndex:
            Integer type.
            start_index points to the first element to be sorted.
            end_index points to the position after the last element to be sorted.
        tartet:
            The list that stores the result.
    """	
    if end_index - start_index > 1:
        # Devide the problem into two sub-questions and apply merge_sort().
        middle = (start_index + end_index) / 2
        merge_sort(source, start_index, middle, target)
        merge_sort(source, middle, end_index, target)

        # Merge to sorted sequences obtained from merge_sort().
        i = start_index		# pointer to the first sub-sequence
        j = middle			# pointer to the second sub-sequence
        k = start_index		# pointer to target
        while i < middle or j < end_index:
            if j >= end_index or (i < middle and source[i] <= source[j]):
                target[k] = source[i]
                i = i + 1
                k = k + 1
            else:
                target[k] = source[j]
                j = j + 1
                k = k + 1
        for i in range(start_index, end_index):
            source[i] = target[i]



#######################   Insert Sort   #######################


def insert_sort(source, start, end):
    """
    Function Descripiton:
        inset_sort(source) takes a list as input, sort the list using insert sort method.
    Parameter Type:
        source:
            The list of objects that can be compared with operator < <= == >= >
    """
    if end - start <= 1:
        return
    else:
        for i in range(start + 1, end):
            temp = source[i]
            j = i
            while j > 0 and source[j - 1] > temp:
                # j starts from i to 1
                source[j] = source[j - 1]
                j = j - 1
            source[j] = temp


#######################  Heap Sort  #######################


def heap_sort(source):
    """
    Function Descripiton:
        heap_sort(source) takes a list as input.
    Parameter Type:
        source:
            The list to be sorted.
    """
    build_max_heap(source)
    for i in xrange(len(source)- 1, 0, -1):
        # i starts from heap_size - 1 to 1
        temp = source[0]
        source[0] = source[i]
        source[i] = temp
        max_heapify(source, 0, i)


def max_heapify(source, i, heap_size):
    """
    Function Descripiton:
        max_heapify(source, i, heap_size) descend the position of the
        element i in a heap with size of heap_size to maintain the max
        property of the heap.
    Parameter Type:
        source:
            The heap.
        i:
            The element whose position we want to descend.
        heap_size:
            The size of the heap. The index of elements that bubbles up
            to replace i should not be less than heap_size.
    """
    lc = 2 * i + 1
    rc = 2 * i + 2
    if lc < heap_size and source[lc] > source[i]:
        largest = lc
    else:
        largest = i
    if rc < heap_size and source[rc] > source[largest]:
        largest = rc
    if largest is not i:
        temp = source[i]
        source[i] = source[largest]
        source[largest] = temp
        max_heapify(source, largest, heap_size)


def build_max_heap(source):
    """
    Function Descripiton:
        build_max_heap(source) build the initial max heap by
        applying max_heapify method from the last node that
        is not a leaf down to the root of the heap.
    Parameter Type:
        source:
            The heap.
    """
    heap_size = len(source)
    for i in xrange(heap_size / 2 - 1, -1, -1):
        # i start from  |_n/2_| - 1  to 0
        max_heapify(source, i, heap_size)


#######################   Randomized Quick Sort   #######################


def normal_quick_sort(source, start, end):
    if end - start > 1:
        middle = partition(source, start, end)
        normal_quick_sort(source, start, middle)
        normal_quick_sort(source, middle + 1, end)


def randomized_quick_sort(source, start, end, target=None, d=None):
    """
    Function Descripiton:
        randomized_quick_sort(source, start, end) takes the list source
        and index start and end as input, and sort [start, end) elements in
        source using quick sort method in acsending sequence and stores the
        result in source itself.
    Parameter Type:
        source:
            The list to be sorted.
        start:
            The start index.
        end:
            The end index.
    """
    if end - start > 1:
        middle = randomized_partition(source, start, end)
        randomized_quick_sort(source, start, middle)
        randomized_quick_sort(source, middle + 1, end)


def partition(source, start, end):
    """
    Function Descripiton:
        partition(source, start, end) partition elements in
        source in range [start, end), and the key element is
        source[end - 1].
    Parameter Type:
        source:
            The list to be sorted.
        start:
            The start index.
        end:
            The end index.
    """
    key = source[end - 1]
    i = start - 1
    for j in xrange(start, end - 1):
        if source[j] <= key:
            i = i + 1
            temp = source[i]
            source[i] = source[j]
            source[j] = temp
    temp = source[i+1]
    source[i+1]=source[end-1]
    source[end-1]=temp
    return i + 1


def randomized_partition(source, start, end):
    """
    Function Descripiton:
        randomized_partition(source, start, end) partition source[start, end)
        using a random element in source[start, end) to be the key element.
    Parameter Type:
        source:
            The list to be sorted.
        start:
            The start index.
        end:
            The end index.
    """
    i = random.randint(start, end - 1)
    temp = source[i]
    source[i] = source[end-1]
    source[end-1] = temp
    return partition(source, start, end)


#######################   Radix Sort   #######################


def radix_sort(source):
    """
    Function Descripiton:
        radix_sort(source) takes the list source as input and sort it
        using radix sort method. For each digit, we use couting sort
        method to obtain the sorted sequence.
    Parameter Type:
        source:
            The list to be sorted.
    """
    length = len(source)
    result = [0 for i in xrange(length)]
    base = 1
    digit_pos = [0 for i in xrange(10)]
    digit = [0 for i in xrange(length)]

    while True:

        # counting sort part
        for i in xrange(length):
            digit[i] = (source[i] / base) % 10
            digit_pos[digit[i]] += 1

        if digit_pos[0] == length:
            break;

        for i in xrange(1, 10):
            digit_pos[i] += digit_pos[i - 1]

        for i in xrange(length - 1, -1, -1):
            # i starts from length - 1 to 0
            pos = digit_pos[digit[i]] - 1
            result[pos] = source[i]
            digit_pos[digit[i]] -= 1

        source = copy.deepcopy(result)
        digit_pos = [0 for i in xrange(10)]

        base *= 10

    return result


def radix_sort_niubi(source, d):
    for k in xrange(d):
        s=[[] for i in xrange(10)]
        for i in source:
            s[i/(10**k)%10].append(i)
        source=[a for b in s for a in b]
    return source