#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
def reverse(text):
    '''Helper function to reverse a string'''
    str_reverse =''
    for i in text:
        str_reverse = i + str_reverse
    return str_reverse

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # if len(text) == 0 or len(text)== 1:
    #     return True

        #reverse the text
    upside_down = reverse(text)
    #haky but for 2 letter comparisons
    # if len(text)==2:
    #  return(text[::-1]==text[::1])

    #starting at t the back of the string
    sentinel= len(text) -1
    usd_count = 0

    while sentinel >= 0:
        if text[sentinel]== upside_down[usd_count]:
          #print(text[sentinel] +' '+upside_down[usd_count] )
          sentinel= sentinel -1
          usd_count= usd_count + 1
          continue
        else: return False
    return True








    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if len(text) == 0 or len(text)== 1:
        return True
    if right == 1: return True
    #reverse the text
    upside_down = reverse(text)
    #haky but for 2 letter comparisons
    # if len(text)==2:
    #  return(text[::-1]==text[::1])

    #starting at t the back of the string
    right= len(text) -1
    left = 0
    while right >= 0:
        if text[right]== upside_down[left]:
          #print(text[sentinel] +' '+upside_down[usd_count] )
          right= right -1

          left= left + 1
          return is_palindrome_recursive(text, right , left)
        else: return False
    return True

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
