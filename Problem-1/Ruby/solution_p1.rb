#!/usr/bin/ruby

def find_sum(num)
	sum = 0
	for i in 3..(num-1)
		if ((i % 3 == 0) or (i % 5 == 0)):
			sum += i
		end	
	end
	return sum
end

$sum10 = find_sum(10)
raise "find_sum is wrong with input 10" unless $sum10 == 23

$sum1000 = find_sum(1000)
puts $sum1000

