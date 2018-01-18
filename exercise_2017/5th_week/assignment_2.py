

WRITE_CODE = False
# 1. 곱셈 함수(꼬리 재귀)
def mult1(m,n):
	def loop(n,ans):
		if (n>0):
			return loop(n-1,m+ans)
		else:
			return ans
	return loop(n,0)
  
# 2. 곱셈 함수(while문)
def mult2(m,n):
	ans = 0
	while (n>0):
		ans += m
		n = n-1
	return ans

###################
#      수정 X      #
# 곱셈 함수 보조 함수 #
def double(n):    #
  return n * 2    #
                  #
def halve(n):     #
  return n // 2   #
###################

# 3. 빠른 곱셈 함수(재귀)
def fastmult1(m,n):
	if n > 0:
		if n % 2 == 0:
			return fastmult1(double(m),halve(n))
		else:
			return m + fastmult1(m,n-1)
	else:
		return 0
  
# 4. 빠른 곱셈 함수(꼬리 재귀)
def fastmult2(m,n):
	def loop(m,n,ans):
		if (n > 0):
			return loop(m,n-1,ans+m)
		else:
			return ans
	return loop(m,n, 0)

# 5. 빠른 곱셈 함수(while문)=
def fastmult3(m,n):
	ans = 0
	while(n > 0):
		ans += m
		n = n-1
	return ans

# 6. 러시아 농부 곱셈 함수(재귀)
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
  
# 7. 러시아 농부 곱셈 함수(꼬리 재귀)
def russianmult2(m,n):
	def loop(m,n,ans):
		if n%2 ==0:
			return loop(double(m),halve(n),ans)
		elif n==1:
			return m+ans
		else:
			return loop(double(m),halve(n),m+ans)
	if n==0:
		return 0
	else:
		return loop(m,n,0)
		
# 8. 러시아 농부 곱셈 함수(while문)
def russianmult3(m,n):
	ans = 0
	while n>0 :
		if n%2 == 0:
			m = double(m)
			n = halve(n)
		elif n == 1 :
			ans += m
			n = halve(n)
		else :
			ans += m
			m = double(m)
			n = halve(n)
	return ans
