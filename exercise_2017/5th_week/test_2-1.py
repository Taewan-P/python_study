def mult1(m,n):
	def loop(n,ans):
		if (n>0):
			return loop(n-1,m+ans)
		else:
			return ans
	return loop(n,0) #왜 0이 되어야 할까...
print(mult1(3,6))