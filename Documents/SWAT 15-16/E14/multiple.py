#multiple of 3 or 5

def main():
	sum = 0
	for i in range(1000):
		if i%3 == 0 or i%5 == 0:
			sum += i
	print sum 
main()
		