import sys      # Used for argument.
import time     # Used for timing functions.

counter = 0 

def get_median(array, left, right):
    a = array[left]
    b = array[int((right + left) / 2)]
    c = array[right]
    if a < b:
        if a < c:
            if b < c:
                return int((right + left) / 2)
            else: return right
        else: return left
    else: 
        if a > c:
            if b > c:
                return int((right + left) / 2)
            else: return right
        else: return left

def quick_sort(array, pivot_type):

    """
    This is quick sort. O(N LOG(N))
    A very fast in place sorting algorithm that works best when a good pivot position
    is chosen. It has an average case of O(N LOG(N)), and a worst case of O(N^2).
    """

    def partition(array, left, right):
        global counter
        counter += right - left 

        
        if pivot_type == 'median':
        	median = get_median(array, left, right)
        	array[left], array[median] = array[median], array[left]

        elif pivot_type == 'last':
        	array[left], array[right] = array[right], array[left]

        pivot = array[left]
        i = j = left + 1
        while j <= right:
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
            j += 1
        array[left], array[i-1] = array[i-1], array[left]
        return i-1

    def q_sort(array, left, right):
        if left <= right:
            # Partition the list
            index = partition(array, left, right)
            #sort both sides recursively
            q_sort(array, left, index -1)
            q_sort(array, index+1, right) 

    global counter
    counter = 0
    if len(array) == 1: return
    q_sort(array, 0, len(array) -1)

def time_me(function, argument, type):

    """This function times other functions."""
    start = time.perf_counter()
    function(argument, type)
    end = time.perf_counter()
    return end - start

#####################################################################

#If no file input, exit.
if len(sys.argv) == 1:
    print("Please pass in a file. Exiting!")
    sys.exit(1)

List = []

# Open file as read only, append each line to array.
with open(sys.argv[1], 'r') as f:
    for line in f:
        List.append(int(line))

arr_first = list(List)
arr_last = list(List)
arr_median = list(List)

time_first = time_me(quick_sort, arr_first, 'first')
comp_first = counter
time_last = time_me(quick_sort, arr_last, 'last')
comp_last = counter
time_median = time_me(quick_sort, arr_median, 'median')
comp_median = counter


print("%-15s %-15s %-15s %-15s" % ('Pivot:', 'First', 'Last', 'Median'))
print("%-15s %-15d %-15d %-15d" % ('Comparisons:', comp_first, comp_last, comp_median))
print("%-15s %-15f %-15f %-15f" % ('Seconds:', time_first, time_last, time_median))





