def find_sum(num):
    sum = 0
    for i in range(num):
        if ((i % 3 == 0) or (i % 5 == 0)):
            sum += i
    return sum

assert(find_sum(10) == 23)

if __name__ == "__main__":
    find_sum(1000)
