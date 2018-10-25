import random

def build_random_list(items, max_value):
    """
    create and return a list filled with items number of element
    each element should be a random integer value
    between 0 and 99
    """
    l = []
    while len(l) < items:
        l.append(random.randint(0, max_value))
        l = l + [random.randint(0, max_value)]
    return l
print(build_random_list(100, 10))

def max(l):
    largest = 0
    for item in l:
        if item > largest:
            largest = item
        return 