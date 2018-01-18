def double(n):    
  return n * 2    

def halve(n):     
  return n // 2   

#첫번째 케이스
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

##########################################

#두번째 케이스

def russianmult2_2(m,n):
	def loop(m,n,ans):
		if n>1:
			if n%2 ==0:
				return loop(double(m),halve(n),ans)
			elif n==1:
				return m+ans
			else:
				return loop(double(m),halve(n),m+ans)
		elif n==0:
			return 0
		else:
			return loop(m,n,0)





def russianmult3(m,n):
    ans = 0
    while n>0 :
        if n%2 == 0:
            m = m*2
            n = n//2
        elif n == 1 :
            ans = ans + m
            n = n//2
        else :
            ans = ans + m
            m = m*2
            n = n//2
    return ans


print(russianmult3(57,86))