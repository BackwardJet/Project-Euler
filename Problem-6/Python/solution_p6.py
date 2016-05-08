def sum_of_squares(num):
	sum = 0
	for i in range(1,num+1):
		sum += (i**2)
	return sum

assert(sum_of_squares(10) == 385)

def square_of_sum(num):
	sum = 0
	for i in range(1,num+1):
		sum += i
	result = sum**2
	return result

assert(square_of_sum(10) == 3025)

def run(num):
	return (square_of_sum(num) - sum_of_squares(num))

assert(run(10) == 2640)

if __name__ == "__main__":
	print(run(100))
