def double(n):    
  return n * 2    

def halve(n):     
  return n // 2   




def russianmult1(m,n):

	def loop(m,n):
		if (n > 1):
			if (n%2 != 0): # n이 홀수
				return m+loop(m, n-1)
			else:
				return loop(double(m),halve(n))
				
		else: # n == 1
			return m
	if (n > 0):
		return loop(m,n)
	else:
		return 0
print(russianmult1(41,25))