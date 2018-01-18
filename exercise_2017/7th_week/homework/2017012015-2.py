def bin_search_closest(ss,key): # bin_search를 확장하여 위치번호도 나오게끔 해라.
    low = 0
    high = len(ss) - 1
    
    while high - low >= 1 :
        mid = (high + low) // 2
        if key == ss[mid]:
            return mid
        elif key < ss[mid]:
            high = mid - 1
        else:
            low = mid + 1
        if high - low ==1:
            if abs(key - ss[low]) > abs(key - ss[high]):
                return high
            elif abs(key - ss[low]) < abs(key - ss[high]):
                return low
        elif high - low == 0:
            return low
    return None


def testcase():
	db = [3260, 74, 3341, 8122, 6179, 4277, 3266, 5025, 1177, 239, 3561, 1827, 4294, 2766, 2969, 2517, 4189, 3066, 5044, 9623]
	db.sort()
	print("CASE 1")
	print("Expect: The closest value to 70 : 74 at index 0")
	key = 70
	index = bin_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 0:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 2")
	print("Expect: The closest value to 3263 : 3260 at index 8")
	print("    OR: The closest value to 3263 : 3266 at index 9")
	key = 3263
	index = bin_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 8 or index == 9:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 3")
	print("Expect: The closest value to 9891 : 9623 at index 19")
	key = 9891
	index = bin_search_closest(db,key)
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
	index = bin_search_closest([],key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Correct")

testcase()