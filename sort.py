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


def insert_sort(source):
    """
    Function Descripiton:
        inset_sort(source) takes a list as input, sort the list using insert sort method.
    Parameter Type:
        source:
            The list of objects that can be compared with operator < <= == >= >
    """
    if len(source) <= 1:
        return
    else:
        for i in range(1, len(source)):
            temp = source[i]
            j = i
            while j > 0 and source[j - 1] > temp:
                # j starts from i to 1
                source[j] = source[j - 1]
                j = j - 1
            source[j] = temp
