# fibonacci adder

def main():
	sum = 0
	x = 1   # 
	y = 2
	while y <= 4000000:
		if y%2 == 0:
			sum += y
		z = y      #place holder for second variable value
		y += x     #generates next value of fib, places it in Y
		x = z      #moves previous current fib value to second place fib value
	print sum
main()
	