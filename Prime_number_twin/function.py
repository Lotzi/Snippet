def check_is_prime(a):
    x = True
    for i in (2, a):
        while x:
            if a % i == 0:
                x = False
            else:
                x = True
    if x:
        return True
    else:
        return False