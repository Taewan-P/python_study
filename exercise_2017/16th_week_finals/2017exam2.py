# -*- coding: utf-8 -*-
##### 0 #####

def count_elements(xss):
	counter = 0
	for x in xss:
		if isinstance(x,list):
			counter += count_elements(x)
		else:
			counter += 1
	return counter

# TEST CASES
# print(count_elements([]))
# print(count_elements([1,2,2]))
# print(count_elements([1,[2],2]))
# print(count_elements([1,[1,2,[1,4]]]))
# print(count_elements([[[[[[[],[[3,2,3]],3]]]]]]))
# print(count_elements([[[[3]],[3]],5,3,[7]]))
# print(count_elements([1,[5,2],[[3],[5,4]],[[[5,5,5,5]]],6,[5,[[5],[[9]]]]]))

# RESULTS
# 0
# 3
# 3
# 5
# 4
# 5
# 14

##### 1 #####

def flatten(xss):
	flat = []
	for x in xss:
		if isinstance(x,list):
			#리스트 일때 리스트를 벗기게끔 재귀?같은걸 써보자
			a = flatten(x)
			
			for i in a:
				flat.append(i)
		else:
			flat.append(x)
	# flat.sort()
	return flat

# TEST CASES
# print(flatten([])) 
# print(flatten([1,2,3])) 
# print(flatten([1,[],3])) 
# print(flatten([1,[1,2,[3,4]]])) 
# print(flatten([[[[[[[[1,2,3]]]]]]]])) 
# print(flatten([[[[3]],[4]],5,6,[7]])) 
# print(flatten([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]])) 

# RESULTS
# []
# [1, 2, 3]
# [1, 3]
# [1, 1, 2, 3, 4]
# [1, 2, 3]
# [3, 4, 5, 6, 7]
# [1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]

#### 2 ####

def identity(mat):
	size = len(mat)
	a = 0
	num = 0
	
	for i in mat:
		if i[num] == 1:
			a += 1
		num += 1
	
	if a == size:
		return True
	else:
		return False

xs0 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
xs1 = [[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]]
xs2 = [[0,-3,6,4],[3,0,-9,8],[-6,9,0,2],[-4,-8,-2,0]]
xs3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# TEST CASES
# print(identity(xs0))
# print(identity(xs1))
# print(identity(xs2))
# print(identity(xs3))

# RESULTS
# True
# False
# False
# False

##### 3 #####

def ascii_art(n):
	for i in range(n):
		for j in range(n):
			print('#', end=' ')
		print()

# TEST CASE
# ascii_art(5)

## (1) ## +
def ascii_art_cross(n):
	for i in range(n):
		for j in range(n):
			if j == n//2 or i == n//2:
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
# ascii_art_cross(5)

## (2) ## X
def ascii_art_X(n):
	for i in range(n):
		for j in range(n):
			if i + j == (n-1) or i == j:
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
# ascii_art_X(5)

## (3) ## 
def ascii_art_square(n):
	for i in range(n):
		for j in range(n):
			if i == 0 or i == (n-1) or j == 0 or j == (n-1):
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
# ascii_art_square(5)

## (4) ## 
def ascii_art_diamond(n):
	mid = n // 2
	for i in range(n):
		for j in range(n):
			if i + j == mid or i + j == mid + (n-1) or abs(i-j) == mid: # fill your logical expression code here
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
# ascii_art_diamond(5)


##### 4 #####
## (1) ##
def substrings_of_length(k,s):
	if k == 0:
		return ['']
	elif 0 < k <= len(s):
		subs = []
		for i in range(len(s)-k+1):
			temp = s[:k]
			subs.append(temp)
			s = s[1:]
		return subs
	else:
		return None

# TEST CASES
# print(substrings_of_length(0,"ERICA"))
# print(substrings_of_length(1,"ERICA"))
# print(substrings_of_length(2,"ERICA"))
# print(substrings_of_length(3,"ERICA"))
# print(substrings_of_length(4,"ERICA"))
# print(substrings_of_length(5,"ERICA"))
# print(substrings_of_length(6,"ERICA"))

# RESULTS
# ['']
# ['E', 'R', 'I', 'C', 'A']
# ['ER', 'RI', 'IC', 'CA']
# ['ERI', 'RIC', 'ICA']
# ['ERIC', 'RICA']
# ['ERICA']
# None

## (2) ##
def substrings(s):
	subs = ['']
	length = len(s)
	for i in range(1,length+1):
		temp = substrings_of_length(i,s)
		for j in range(len(temp)):
			subs.append(temp[j])
	return subs

# TEST CASES
# print(substrings("ERICA"))
# print(substrings(""))

# RESULTS
# ['', 'E', 'R', 'I', 'C', 'A', 'ER', 'RI', 'IC', 'CA', 'ERI', 'RIC', 'ICA', 'ERIC', 'RICA', 'ERICA']
# ['']


##### 5 #####
## (1) ##
def subint_of_length(k,l):
	if k==0:
		return []
	elif 0 < k < len(l):
		subs = []
		for i in range(len(l)-k+1):
			temp = l[:k]
			subs.append(temp)
			l = l[1:]
		return subs
	else:
		return []


def subint(l):
	subs = []
	length = len(l)
	for i in range(1, length + 1):
		temp = subint_of_length(i,l)
		for j in range(len(temp)):
			subs.append(temp[j])
	return subs


def increasing(ns):
	return len(ns) < 2 or ns[0] < ns[1] and increasing(ns[1:])


def longest_ascending_sublist(ns):
	a = subint(ns)
	num = 0
	ans = []
	for i in a:
		if increasing(i) and num < len(i):
			num = len(i)
			ans = i
	return ans



# TEST CASES
# print(longest_ascending_sublist([1,5,3,4,8,2,3,5]))
# print(longest_ascending_sublist([]))
# sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
# print(longest_ascending_sublist(sample))

# RESULTS
# [3, 4, 8]
# []
# [28, 37, 61, 66, 89]

## (2) ##
def longest_steepest_ascending_sublist(ns):
	def slope(ns):
		return (ns[-1] - ns[0]) / len(ns)
	a = subint(ns)
	num = 0
	b = 0
	ans = []
	for i in a:
		if (increasing(i) and num <= len(i)):
			num = len(i)
			temp = i
			if  b < slope(temp):
				b = slope(temp)
				ans = temp
			else:
				b = 0
	return ans
	


# TEST CASES
# print(longest_steepest_ascending_sublist([1,5,3,4,8,2,3,5]))
# print(longest_steepest_ascending_sublist([]))
# sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
# print(longest_steepest_ascending_sublist(sample))

# RESULTS
# [3, 4, 8]
# []
# [7, 23, 34, 67, 77]

