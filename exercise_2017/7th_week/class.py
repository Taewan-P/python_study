#4월 13일 목요일 수업시간
def seq_search(s,key):
	if s != []:
		if s[0] == key:
			return True
		else:
			return seq_search(s[1:],key)
	else:
		return False

def seq_search1(s,key):
	while s != []:
		if s[0] == key:
			return True
		else:
			s = s[1:]
	return False

def seq_search2(s,key):
	i = 0
	for x in s:
		if x == key:
			return i
		i += 1
	return None #False 로 해도 되고 -1 이라고 해도 된다.

def seq_search2_1(s,key):
	for i in range(len(s)):
		if s[i] == key:
			return i
	return False

def bin_search(ss,key):
	if ss != []:
		mid = len(ss) // 2
		if key == ss[mid]:
			return True
		elif key < ss[mid]:
			return bin_search(ss[:mid],key) #처음부터 mid 전까지 다시 돌린다.
		else:
			return bin_search(ss[(mid+1):],key) #mid 다음부터 다시 돌린다.
	return False

def bin_search1(ss,key):
	while ss != []:
		mid = len(ss) // 2
		if key == ss[mid]:
			return True
		elif key < ss[mid]:
			ss = ss[:mid] #원래 리스트를 mid 전까지 있는걸루 대체한다.
		else:
			ss = ss[mid+1:] #원래 리스트를 mid다음부터 끝까지로 대체한다.
	return False

def bin_search2(ss,key):
	low = 0
	high = len(ss)-1
	while low <= high:
		mid = (high+low) // 2
		if key == ss[mid]:
			return True
		elif key < ss[mid]:
			high = mid - 1 
		else:
			low = mid + 1
	return None

def find_first(filename,key):
	infile = open(filename, "r")
	outfile = open("output.txt", "w")
	
	s= infile.read()
	pos = s.find(key)
	if pos == -1:
		# not found
		outfile.write(key + " is not found\n")
	else:
		outfile.write(key + " is found at" + str(pos) + "\n")


	outfile.close() # 여는 코드를 쓰고 바로 닫는 코드를 쓰는걸 권장한다.
	infile.close()

def find_second(filename,key):
	infile = open(filename, "r")
	outfile = open("output.txt", "w")
	
	s= infile.read()
	pos = s.find(key)
	pos = s.find(key,pos+1)
	if pos == -1:
		outfile.write(key + " is not found\n")
	else:
		outfile.write(key + " is found at" + str(pos) + "\n")


	outfile.close()
	infile.close()


