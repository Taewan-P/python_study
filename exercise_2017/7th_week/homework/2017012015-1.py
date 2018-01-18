def seq_search_closest(s,key):
	random_list  = []
	for i in range(0,len(s)):
		random_list.append(abs(key-s[i]))
	random_list.sort()
	for i in range(0,len(s)):
		if (key + random_list[0]) == s[i] or (key - random_list[0]) == s[i]:
			return i


def testcase():
	db = [3260, 74, 3341, 8122, 6179, 4277, 3266, 5025, 1177, 239, 3561, 1827, 4294, 2766, 2969, 2517, 4189, 3066, 5044, 9623]
	print("CASE 1")
	print("Expect: The closest value to 70 : 74 at index 1")
	key = 70
	index = seq_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 1:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 2")
	print("Expect: The closest value to 3263 : 3260 at index 0")
	print("    OR: The closest value to 3263 : 3266 at index 6")
	key = 3263
	index = seq_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 0 or index == 6:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 3")
	print("Expect: The closest value to 9891 : 9623 at index 19")
	key = 9891
	index = seq_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 19:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 4")
	print("Expect: 9891 found at None")
	key = 9891
	index = seq_search_closest([],key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Correct")

testcase()