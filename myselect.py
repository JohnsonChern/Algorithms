import copy
import sort

def randomized_select(source, start, end, k):
    """
    Function Description:
        randomized_select selects the kth least number from source using
        randomized method.
        Note that all indeces are absolute starting from 0.
    """
    if len(source) < k:
        return "wrong index k"
    i = sort.randomized_partition(source, start, end)
    if i == k - 1:
        return source[i]
    elif i > k - 1:
        return randomized_select(source, start, i, k)
    else:
        return randomized_select(source, i + 1, end, k)


def select(source, start, end, k):
    if (end - start) <= 140:
        sort.normal_quick_sort(source, start, end)
        return [source[k - 1], k-1]
    length = end - start

    for i in xrange(length/5):
        sort.insert_sort(source,start + i*5, start + i*5 + 5)
        temp = source[start + i]
        source[start + i] = source[start + 5*i + 2]
        source[start + 5*i + 2] = temp

    [i, index] = select(source, start, start + length/5, length/10)
    temp = source[index]
    source[index] = source[end - 1]
    source[end - 1] = temp
    j = sort.partition(source, start, end)
    
    if j == k:
        return [source[j], j]
    elif j > k:
        return select(source, start, j, k)
    else:
        return select(source, j + 1, end, k)
