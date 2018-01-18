#4월 6일 목요일 수업시간
#재귀와 반복 - 정렬
def ssort0(s):
	if s != []:
		smallest = min(s)
		s.remove(smallest)
		return [smallest] + ssort0(s)
	else:
		return [] #s 를 넘겨줘도 된다.비어있었으니...
print(ssort0([5,1,2,4,3,5]),'ssort0 출력값')

def ssort1(s):
	def loop(s,ss):
		if s!= []: #ss 가 리스트
			smallest = min(s)
			s.remove(smallest)
			return loop(s,ss+[smallest]) #[smallest] + ss 하면 내림차순
		else:
			return s

	loop(s,[])

def ssort1_1(s):
	def loop(s,ss):
		if s!= []: #ss 가 리스트
			smallest = min(s)
			s.remove(smallest)
			ss.append(smallest)
			return loop(s,ss)
		else:
			return s

	loop(s,[])

#for i in (here)여기에 mutable type 로 돌리면 오류가 생길 가능성이 있다.
def msort(s):
	if len(s)>1:
		mid = len(s) // 2
		left = s[:mid]
		right = s[mid:]
		return merge(msort(left), msort(right))
	else:
		return s

def merge(left,right):
	if not (left ==[] or right ==[]):
		hl = left[0]
		hr = right[0]
		if(hl<hr):
			x = hl
			left = left[1:]
		else:
			x = hr
			right =right[1:]
		return [x] + merge(left,right)
	else:
		return left + right


def qsort(s):#미완성,돌리지 말것.
	if len(s)>1:
		pivot = s[0]
		s = s[1:]
		(left,right) = partition(s.pivot)
		return qsort(left) + [pivot] + qsort(right)
	else:
		return s

def partition(s,pivot):
	left = []
	right = []
	for x in s:
		if x<=pivot:
			left += [x] #left.append(x)
		else:
			right += [x]

	return left, right

print(qsort([5,2,3,1,5]))