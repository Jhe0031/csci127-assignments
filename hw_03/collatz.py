# Partners: Anthony Sokolov & Jia Qi He

def collatz(n):
    """
    if n = 1 stop
    otherwise
    if n is odd --> 3n+1
    if n is even --> n/2
    until n becomes
    """
    print(n)
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        print(n)
        count += 1
    return count

print('Number of Steps:', str(collatz(12)))
print('Number of Steps:', str(collatz(15)))