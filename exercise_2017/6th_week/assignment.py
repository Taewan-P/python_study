#실습1번
def insert1(x,ss):
	if ss != []:
		if x <= ss[0]:
			return [x] + ss #낄자리일때?
		else:
			return [ss[0]] + insert1(x,ss[1:]) #낄자리가 아닐때
	else:
		return [x] #낄자리가 맨 끝일때 

#실습2번
def insert2(x,ss):
	def loop(ss,left):
		if ss != []:
			if x <= ss[0]:
				return left + [x] + ss
			else:
				return loop(ss[1:], left + [ss[0]]) 
				#리스트에서 하나를 뽑으면 숫자 하나기 때문에 대괄호 처리를 꼭 하자.
		else:
			return left + [x]
	return loop(ss,[])

#실습3번
def insert3(x,ss):
	left = []
	while ss != []:
		if x <= ss[0]:
			return left + [x] + ss	#낄 자리일때
		else:
			ss,left = ss[1:], left + [ss[0]] #낄 자리가 아닐때
	return left + [x]

def isort0(s):
	if s!= []:
		return insert3(s[0],isort1(s[1:]))
	else:
		return []

#실습4번 insert 함수사용해!
def isort1(s): #s가 리스트고 ss가 left 같은 존재.
	def loop(s,ss):
		if s != []:
			return loop(s[1:],insert3(s[0],ss)) 
		else:
			return ss
	return loop(s,[])

#실습5번
def isort2(s):
	ss = []
	while s != []:
		s, ss = s[1:], insert3(s[0],ss)
	return ss


#실습6번
#5번 문제를 for 반복문 버전으로 바꾸어 써보자.
def isort3(s):
	ss = []
	for _ in range(len(s)):
		s, ss = s[1:], insert3(s[0], ss)
	return ss

#실습7번
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

#실습8번(코드 확인!)
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


#실습9번
def bsort(s):
	for k in range(len(s)-1):
		for i in range(len(s)-1):
			if s[i] > s[i+1]:
				s[i],s[i+1] = s[i+1],s[i]
	return s
	

x1 = 4
x2 = 8
ss = [1,3,6,7]
s = [4,7,2,5,9,1]
left = [1,4,5,8]
right = [2,3,6,9]

print("insert1(x,ss)", insert1(x1,ss))
print("insert1(x,ss)", insert1(x2,ss))
print("insert2(x,ss)", insert2(x1,ss))
print("insert2(x,ss)", insert2(x2,ss))
print("insert3(x,ss)", insert3(x1,ss))
print("insert3(x,ss)", insert3(x2,ss))
print("isort1(s)", isort1(s))
print("isort2(s)", isort2(s))
print("isort3(s)", isort3(s))
print("merge1(left,right)", merge1(left,right))
print("merge2(left,right)", merge2(left,right))
print("bsort(s)", bsort(s))

