#3월 30일 목요일 수업시간
import time

def countdown(n):
	if n>0:
		if n <10 and n%2 == 0:
			print('발사임박!')
		else:
			print(n)
		time.sleep(1)
		countdown(n-1)
	else:
		print('발사!')

def countdown_iter(n):
	while n>0:
		if n<10 and n%2 == 0:
			print('발사임박!')
		else:
			print(n)
		time.sleep(1)
		n = n-1
	print('발사!')

def sigma(n):
	if n>0:
		return n+sigma(n-1)
	else:
		return 0

def sigma_tail(n):
	def loop(n,sum):
		if n>0:
			return loop(n-1, n+sum)
		else:
			return sum
	return loop(n, 0)

def sigma_iter(n):
	sum = 0
	while n>0:
		sum += n
		n = n-1
	return sum

def sumrange(m,n):
	if m<n:
		m+sumrange(m+1,n)
	else:
		return n

def sumrange_tail(m,n):
	def loop(m,n,sum):
		if m<=n:
			return sumrange(m+1,n,sum+m)
		else:
			return sum
	return loop(m,n,0) #비용이 아주 큰 코드

def sumrange_iter(m,n):
	sum = 0
	while m <= n: #메모리 사용량이 아주 좋다는점.(tail보다.)
		sum += m
		m += 1
	return sum

def fact(n):
	if n>0:
		return n*fact(n-1)
	else:
		return 1

def fact_tail(n):
	def loop(n,prod):
		if n>0:
			return loop(n-1, n*prod)
		else:
			return prod
	loop(n,1)

def fact_iter(n):
	prod = 1
	while n>0:
		prod *= n
		n -=1
	return prod

def pow(b,n):
	if n>0:
		return n*pow(b,n-1)
	else:
		return 1

def pow_1:
	if n>0:
		if n%2 == 0:
			return pow(b**2 , n//2)
		else:
			return b*pow(b,n-1)
	else:
		return 1#pow 보다 pow_1 이 얼마나 빠를까에 대하여 생각해 보자.
