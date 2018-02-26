    #!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    #return linear_search_recursive(array, item)


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
    if index ==len(array)-1:
        return None
    else:
        return linear_search_recursive(array, item, index+ 1)
    #since its a lenear and not binary i shiuld jsut have to add 1 to the index and it should woulr


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
    #the purpose of this is that before the recursion starts the values of left right and mid arent defined, for the fist ieration thye have to be defined as the length of the list, since that is what we're checking
    if left == None and right == None:
        left = 0
        right = len(array) -1
    elif left > right:
      #basically a check for iff there is anything in the list at all
      return None
      #for each ineation this defines the middle as the left value ( which is mutable) - the rigth value( which is mutable)
    mid = int((left + right) / 2)
    #if the item is  the middle value
    if item == array[mid]:
        return mid
    # if the item is smaller than the item at the mid point, the left is static, but the new right( end of the check in the array), is now the middle -1( since we know it isnt in that side of the list)
    elif item < array[mid]:
        return binary_search_recursive(array, item, left, mid - 1)
    else:
        #if the item is larger than the mid value, the new array range to check is now, from the middle plus 1 all the way to the defined end
        return binary_search_recursive(array, item, mid + 1, right)
    # if it aint found, then tell is it isnt
    return None
