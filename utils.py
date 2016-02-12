
'''
By Jason Krone for Khan Academy

Implementation of subset sum Utils
'''

BASE_TUPLE = (True, 0, 0)

def subset_sum_within_range(nums, n, delta):
    ''' 
    returns a subset of the given numbers that sum within the given range
    (n - delta, n + delta) if such a subset exists.  Otherwise, returns None
    '''
    assert nums

    subset = None
    subset_sum_arr = positive_subset_sum_table(nums, n + delta)

    # loop through values in range n - k to n + k
    for i in range(n - delta, n + delta + 1):
        # check if there is a sum set sum to i
        if type(subset_sum_arr[i]) is tuple and subset_sum_arr[i] != BASE_TUPLE:
            # get the subset that sums to i
            subset = get_subset_with_sum(subset_sum_arr, i)
            break

    return subset


def get_subset_with_sum(table, n):
    '''
    returns the subset of numbers listed in the table that sum to n
    '''
    assert table

    subset = []
    i = n

    while i > 0:
        subset.append(table[i][1])
        i = table[i][2]

    return subset


def positive_subset_sum_table(A, x):
    '''
    attribution: this code was modified from
    http://www.geekviewpoint.com/python/dynamic_programming/positive_subset_sum
    '''
    assert A
 
    # algorithm
    sub_sum = [None] * ( x + 1 )
    sub_sum[0] = BASE_TUPLE
    p = 0
    while not sub_sum[x] and p < len( A ):
        a = A[p]
        q = x
        while not sub_sum[x] and q >= a:
            if not sub_sum[q] and sub_sum[q - a]:
                sub_sum[q] = (True , a, q - a)
            q -= 1
        p += 1
    return sub_sum


