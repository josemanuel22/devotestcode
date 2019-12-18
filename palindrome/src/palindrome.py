
def is_palindrome(string):
    """
    Check if a sring is palindrome
    :param string: string to check if is palindrome
    :type string: string
    :return: True if the string is palindrome, False if not.
    """
    i=0
    n=int(len(string)/2)
    for letter in string[0:n-1]:
        i+=1
        if letter != string[-i]:
            return False
    return True




