def divide(A, B, u):
    slice = (A/B)*u
    i = 0
    while i < 10:
        if i*slice == 1:
            invitees = i
            break
        i += 1
    return invitees
print('Invitees:', divide(5, 10, 1))
print('Invitees:', divide(4, 8, 2))
print('Invitees:', divide(5, 10, .5))