def run():
	i = 0
	while True:
	
		for j in range(11,21): # 11 to 20
			if (i % j != 0):
				break
			if (j == 20):
				return i
		i += 1

print(run())


'''
NOTES:
20 - 2,4,5,10
19 - 19
18 - 2,3,6,9
17 - 17
16 - 2,4,4,8
15 - 15
14 - 2,7
13 - 13
12 - 2,6
11 - 11
'''	
