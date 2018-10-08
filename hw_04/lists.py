import random

def build_random_list(size, max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = []
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i + 1
    return l
l = build_random_list(10, 20)
print('l:', l)

print('Set value: 5')

def locate(l, value):
    """
    This routine should accept a list as the first parameter and a value for the
    second. The function will look for value in the list and return it’s index.
    Return -1 if value isn’t in the list.
    """
    if value in l:
        i = 0
        while i < len(l):
            if l[i] == value:
                i += 1
                return i
            i += 1
    return -1
print('Index value:', locate(l, 5))
    
def count(l, value):
    """
    This routine should accept a list as the first parameter and a value for the
    second. It should return the number of times value appears in the list l.
    """
    if value in l:
        num = 0
        i = 0
        while i < len(l):
            if l[i] == value:
                num += 1
            i += 1
        return num
    else:
        print("Value is not in list")
print('Number of appearances:', count(l, 5))

def reverse(l):
    """
    This function should accept a list as its parameter. It will build and return
    a new list which has the same elements as the original but with the values
    reversed.
    """
    i = 1
    l_rev = []
    while i <= len(l):
        value = l[-i]
        l_rev.append(value)
        i += 1
    return l_rev
print('Reversed l:', reverse(l))

def isIncreasing(l):
    """
    This function should accept a list as its parameter. It will return True if
    the list is strictly increasing, that is starting with the first element,
    each successive element is greater than the previous. For example, the list
    1,5,10,11,13 is increasing while 1,5,3,6 and 1,4,4,6 are not.
    """
    i = 0
    while i < len(l):
        if l[i] < l[i+1]:
            i += 1
            continue
        elif l[i] >= l[i+1]:
            return False
        return True
print('List increasing: ' + str(isIncreasing(l)))
    
def palindrome(l):
    """
    This function should return True if the list represents a palindrome and
    False otherwise. A list is a palindrome if it has the same elements left to
    right as it does right to left.
    """
    if l == reverse(l):
        return True
    elif l != reverse(l):
        return False
print('Palindrome: ' + str(palindrome(l)))
    