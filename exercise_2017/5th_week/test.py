def fastmult3(m,n):
	ans = 0
	while(n > 0):
		ans += m
		n = n-1
	return ans
print(fastmult3(3,6))