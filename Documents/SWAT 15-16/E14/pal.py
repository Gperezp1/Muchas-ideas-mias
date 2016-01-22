# pal

def main():
	palindromes = []
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			test = i*j
			s = str(test)
			
			if test >= 100000:
				if s[0] == s[5] and s[1] == s[4] and s[2] == s[3]:
					palindromes.append(test)
			if test <= 100000:
				if s[0] == s[4] and s[1] == s[3]:
					palindromes.append(test)
	answer = max(palindromes)
	print "Answer = %5d" % answer
main()