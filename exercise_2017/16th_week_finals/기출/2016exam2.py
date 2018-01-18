### 반 : 화 / 금
### 이름 :
### 학번 : 

#### 2 ####
# 문자열 내에 특정 문자가 나타나는 횟수를 내주는 함수

def occurred_in(char, string):
	occ = 0
	for c in string:
		if char == c:# fill me in
			occ += 1
	return occ

# print(occurred_in('p', '')) # 0
# print(occurred_in('p', 'I love Python!')) # 0
# print(occurred_in('e', 'What happened to your college life?')) # 5

#### 3 ####

def numbers_art(n):
	for i in range(n):
		for j in range(n):
			print(j+1, end=' ')
		print()

# numbers_art(5)
# numbers_art(7)

# (1)
def numbers_art1(n):
	a = []
	for i in range(n,0,-1):
		a.append(i)
	for i in range(n):
		for j in range(len(a)):
			print(a[j], end = ' ')
		print()
		a = a[1:]


# (2)
def numbers_art2(n):
	a = [1]
	for i in range(1,n+1):
		for j in range(len(a)):
			print(a[j], end = ' ')
		a.append(i+1)
		print()



# (3)
def numbers_art3(n):
	a = []
	for i in range(1,n+1):
		a.append(i)

	for j in range(1,n+1):
		for i in range(len(a)):
			print(a[i], end = ' ')
		print()
		a[j-1] = ' '



# (4)
def numbers_art4(n):
	a = []
	for _ in range(n):
		a.append(' ')
	
	for i in range(n):
		a[n-1] = n
		for j in range(len(a)):
			print(a[j], end = ' ')
		print()
		n -=1



# numbers_art1(5)
# numbers_art2(5)
# numbers_art3(5)
# numbers_art4(5)


##### 4 #####

# 인수 n이 소수인지 확인하기
# def is_prime(n):
# 	if n < 2:
# 		return False
# 	else:
# 		for i in range(2,n):
# 			if n % i == 0:
# 				return False
# 		return True

# for i in range(50):
# 	if is_prime(i):
# 		print(i)

# (1)
def is_prime(n):
	if n ==2:
		return True
	elif n%2 == 0 or n == 1:
		return False
	else:
		for i in range(3,n,2):
			if n % i == 0:
				return False
		return True

# for i in range(50):
# 	if is_prime(i):
# 		print(i)

# (2)
# 자연수 n미만의 소수를 2부터 시작하여 모두 오름차순으로 나열한 리스트로 만들어 내주는 함수
def primes_less_than(n):
	p = []
	for i in range(n):
		if is_prime(i):
			p.append(i)
	return p

# print(primes_less_than(2)) # []
# print(primes_less_than(3)) # [2]
# print(primes_less_than(10)) # [2, 3, 5, 7]
# print(primes_less_than(30)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (3)
# k개의 소수를 2부터 시작하여 오름차순으로 리스트로 만들어 내주는 함수
def primes(k):
	p = []
	n = 2
	while k > 0:
		if is_prime(n):	
			p.append(n)
			k -= 1
		n += 1
	return p

# print(primes(0)) # []
# print(primes(1)) # [2]
# print(primes(5)) # [2, 3, 5, 7, 11]
# print(primes(10)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (4)
# 쌍둥이 소수 k 쌍 찾기 (차이가 2인 소수의 쌍)
def twin_primes(k):
	p = []
	n = 3
	while k > 0:
		if is_prime(n) and is_prime(n+2):
			p.append((n,n+2))
			k -=1
		n += 1
	return p

# print(twin_primes(0)) # []
# print(twin_primes(1)) # [(3, 5)]
# print(twin_primes(5)) # [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31)]
# print(twin_primes(10)) 
# [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109)]


#### 5 ####

# (1)
## generate all subsequences

# def subsequences(ns):
# 	subs = [[]]
# 	for n in ns:
# 		newsubs = []
# 		# print(n)
# 		for sub in subs:
# 			# n = [n]
# 			sub.append(n)
# 			newsubs.append(sub)

# 		subs += newsubs
# 	return subs

#다시 보자.
def subsequences(ns):
	subs = [[]]
	for n in ns:
		newsubs = []
		inssubs = []
		for sub in subs:
			newsubs = sub + [n]
			inssubs.append(newsubs)
		subs += inssubs
	return subs

# print(subsequences([])) 
# [[]]
# print(subsequences([1]))
# [[], [1]]
# print(subsequences([1,2]))
# [[], [1], 
#  [2], [1, 2]]
# print(subsequences([1,2,3]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# print(subsequences([1,2,3,4]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], 
#  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

# (2)
# check if a list is increasing
def increasing(ns):
	return len(ns)<2 or ns[0] < ns[1] and increasing(ns[1:])

# print(increasing([])) # True
# print(increasing([2])) # True
# print(increasing([1,2])) # True
# print(increasing([2,2])) # False
# print(increasing([3,2])) # False
# print(increasing([1,2,3])) # True
# print(increasing([1,3,2])) # False
# print(increasing([3,2,1])) # False

# (3)
# length of longest increasing subsequence
def longest_increasing_subsequence(ns):
	if len(ns) < 2:
		return len(ns)
	else:
		subs = subsequences(ns)
		longest = 1
		for sub in subs:
			length = len(sub)
			if increasing(sub) and length > longest:
				longest = length
		return longest

print(longest_increasing_subsequence([])) # 0
print(longest_increasing_subsequence([3])) # 1
print(longest_increasing_subsequence([5,4])) # 1
print(longest_increasing_subsequence([2,4])) # 2
print(longest_increasing_subsequence([4,3,2])) # 1
print(longest_increasing_subsequence([4,2,7,5,9])) # 3
print(longest_increasing_subsequence([4,2,7,5,4,7,6,8,9,6])) # 5

#### 6 ####

# (1)
# 2진수를 10진수로 바꾸기

def bin2dec(bin):
	length = len(bin)
	dec = 0

	for i in range(length):	
		if bin[i] == '1':
			dec += 2**(length-1)
			length -= 1
		else:
			length -= 1
	return dec

# print(bin2dec('0')) # 0
# print(bin2dec('1')) # 1
# print(bin2dec('110')) # 6
# print(bin2dec('10011')) # 19
# print(bin2dec('101010')) # 42

# (2)
# 10진수를 2진수로 바꾸기

def dec2bin(dec):
	bin = ''
	while not (dec == 0 or dec == 1):
		bin += str(dec % 2)
		dec //=2
	bin = str(dec) + bin
	return bin

# print(dec2bin(0)) #=> '0'
# print(dec2bin(1)) #=> '1'
# print(dec2bin(6)) #=> '110'
# print(dec2bin(19)) #=> '10011'
# print(dec2bin(42)) #=> '101010'



