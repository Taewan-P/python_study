def gcd1_2(m,n):
	print("gcd1_2")
	def loop(m, n, k):
		print("gcd1_2, loop",m,n,k)
		if not(m==0 or n==0):
			if m%2==0 and n%2==0:
				return loop(m//2,n//2,k*2) #오류 발생시 여기 확인!!(빈칸 있는 부분 k)
				
			elif m%2==0 and n%2==1:
				return loop(m//2,n,k)
	
			elif m%2==1 and n%2==0:
				return loop(m,n//2,k)
	
			elif m<=n:
				return loop(m,(n-m)//2,k)
	
			else:
				return loop(n,(m-n)//2,k)

		else:
			if m==0:
				return abs(n*k)
			else:  #n==0
				return abs(m*k)
		
		
	return loop(m,n,1)

print(gcd1_2(18,48))

