#4월 27일 목요일 수업시간
def fib(n):
	if n > 1:
		return fib(n-1) + fib(n-2)
	else:
		return n

def fib1(n): #동적 계획법(dynamic programming) /다시 한번 확인하자!/
	i = 1
	bunny, rabbit = 1, 0
	while i < n:
		bunny, rabbit = rabbit, rabbit + bunny
		i += 1
	return rabbit + bunny

def fib2(n):
	bunny, rabbit = 1, 0
	for _ in range (1,n): # "_" means underscore
		bunny, rabbit = rabbit, rabbit + bunny
	return rabbit + bunny

def fib3(n):
	fibs = [0,1]
	for i in range(2,n+1):
		fibs.append(fibs[i-1] + fibs[i-2])
	return fibs

# print(fib3(10))

def comb(n,r):
	if not (r == 0 or n==r):
		return comb(n-1,r) + comb(n-1, r-1)
	else:
		return 

#Very Hard...
def comb_pascal(n,r):
	#i는 한 행을 가리킨다고 볼 수 있다...
	matrix = [[]] * (n-r+1) #init matrix
	matrix[0] = [1] * (r+1) #fill first row
	
	for i in range(1, n-r+1): #fill first column
		matrix[i] = [1]

	for i in range(1, n-r+1):
		for j in range(1,r+1):
			matrix[i].append(matrix[i][j-1] + matrix[i-1][j]) #왼쪽, 위 순서대로 더하는 구문

	return matrix[n-r][r]


print(comb_pascal(10,5))

def hanoi(n,src,tgt,tmp): #하노이의 탑 : src 가 첫번째, targt이 세번째, 그리고 tmp가 두번째. n 은 탑의 갯수
	cnt = 0
	if n>1:
		hanoi(n-1,src,tmp,tgt)
		print("move : " + src + "->" + tgt)
		cnt += 2*hanoi(n-1,tmp,tgt,src)
		#아니면
		#cnt += 1
		#cnt += hanoi(n-1,tmp,tgt,src) 이런 식으로
	else:
		print("move : " + src + "->" + tgt)
		cnt = 1
	return cnt

# hanoi(3,"s","t","x")
