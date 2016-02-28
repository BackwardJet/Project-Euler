def isPal(var):
    str_var = str(var)
    if (len(str_var) < 2):
        return True
    if (str_var[0] == str_var[-1]):
        return isPal(str_var[1:-1])


def largestPal(num_digits):
    lower = (10**(num_digits-1))
    upper = (10**(num_digits)-1)
    largest = 0
    for i in range(lower,upper+1):
        for j in range(i,upper+1):
            if ((isPal(i*j)) and ((i*j) > largest)):
                largest = i*j
    return largest

assert(isPal(100001))
assert(not isPal('dasq'))
assert(largestPal(2) == 9009)

if __name__ == "__main__":
    print(largestPal(3))
