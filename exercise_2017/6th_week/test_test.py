def insert3(x,ss):
	left = []
	while ss != []:
		if x <= ss[0]:
			return left + [x] + ss	
		else:
			ss,left = ss[1:], left + [ss[0]]
	return left + [x]

def isort0(s):
	if s!= []:
		return insert3(s[0],isort0(s[1:]))
	else:
		return []

def insert_easy(x,ss):
	ss.append(x)
	return sorted(ss)

print(insert3(4,[1,3,6,7]))
print(insert_easy(4,[1,3,6,7]))
print(isort0([4,3,1,6,7]))

def isort2(s):
	def loop(s,ss):
		if s != []:
			return loop(s[1:],insert3(s[0],ss)) 
		else:
			return ss
	return loop(s,[])

def isort3(s):
	ss = []
	while s != []:
		s, ss = s[1:], insert3(s[0],ss)
	return ss


def isort4(s):
	ss = []
	for _ in range(len(s)):
		s, ss = s[1:], insert3(s[0], ss)
	return ss

print(isort3([4,3,1,6,7]))
print(isort4([4,3,1,6,7,9,2]))


def merge1(left,right):
	def loop(left,right,ss):
		if not (left ==[] or right == []):
			if left[0] <= right[0]:
				ss.append(left[0])
				return loop(left[1:],right,ss)
			else:
				ss.append(right[0])
				return loop(left,right[1:],ss)
		else:
			return ss + left + right
	return loop(left,right,[])

print('merge1',merge1([1,4,5,9],[2,3,6,8]))

def merge2(left,right):
	ss =[]
	while not (left ==[] or right == []):
		if left[0] <= right[0]:
			ss.append(left[0])
			left = left[1:]
		else:
			ss.append(right[0])
			right = right[1:]
			
	return ss + left + right

print('merge2',merge2([1,4,5,8],[2,3,6,9]))

def bsort(s):
	for k in range(len(s)-1):
		for i in range(len(s)-1):
			if s[i] > s[i+1]:
				s[i],s[i+1] = s[i+1],s[i]
	return s
print('bsort', bsort([1,2,3,4,5,6,7,8,9]))


