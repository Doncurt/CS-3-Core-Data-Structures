#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    #if you find the item first, then all your work is done before it even begins since that will be o(1)
    #as per the instructions it returns the item
    if array[index]== item:
        #return the index of the item
        return index

    # Asking in youve searched all of the indexis and not found the item in question
    if index ==len(array) :
        return None
    #since its a lenear and not binary i shiuld jsut have to add 1 to the index and it should woulr

    return linear_search_recursive(array, item, index+ 1)

    #UPDATE: IT WORKS!!!!!
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    #declar the upper and lowe bounds
    if len(array)==0 or len(array)==1:
        return 0
    if array[0]== item: return 0
    lower,upper = 0, len(array)-1
    while lower <= upper:
        middle = (lower + upper)// 2 #needed for integer division incase the list is odd numbered
        if array[middle] < item:
            lower = middle + 1
        if item < array[middle]:
            upper = middle -1
        if item == array[middle]:
            return middle
    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests





def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if len(array) == 0:
        return None
    if array[0]== item: return 0
    #learning more about slices
    #slices everything from the middle down the array[0]

    left = array[int(len(array)/2) + 1:]
    #slices everything grom the biggining to the middle defined as half of the length of the array
    right = array[:int(len(array)//2)]

    mid = (array[(int(len(array)/2))])  # integer division for slicing in next step
    if item == mid : return (int(len(array)/2))
    # take the left array
    elif item < mid: return binary_search_recursive(left, item, left= None, right= None)
    #take right slice of the array
    elif item > mid: return binary_search_recursive(right, item, left= None, right= None)
    # if its not found return None since it doesnt exist


    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    else:
      return None
