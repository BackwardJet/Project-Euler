def getFibSum(num):
    results = [] #initialize a list with "num" elements
    sum = 0
    fib = 0
    two_nums_ago = 1
    one_num_ago = 2
    while (fib < num):
        fib = one_num_ago + two_nums_ago
        if (fib > num):
            break
        if (fib % 2 == 0):
            sum += fib
        two_nums_ago = one_num_ago
        one_num_ago = fib
    if (sum != 0):
        sum += 2
    return sum

assert(getFibSum(10) == 10) # 1,2,3,5,8... 2 + 8 = 10
assert(getFibSum(100) == 44) #1,2,3,5,8,13,21,34,55,89... 2 + 8 + 34 = 44 

if __name__ == "__main__":
    print(getFibSum(4000000))
