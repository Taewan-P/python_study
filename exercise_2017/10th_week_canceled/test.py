def split_digit(num):
	a = num
	a.split()
	first = int(a[0])
	second = int(a[1])
	third = int(a[2])
	fourth = int(a[3])
	result = [first, second, third, fourth]
	return result

def anagram(lists):
	list_sort = []
	printer = []
	num = 0
	# hoz = 0
	ver = 0
	
	#4자리 숫자를 한개씩 나눈후 정렬한 뒤에 2차원 배열에 넣기
	
	for i in lists:
		a = split_digit(i)
		a.sort()
		list_sort.append(a)
	
	#정렬된 숫자로 애너그램인지 각 리스트를 비교하기
		list_copy = list_sort
	b = 0
	for j in list_copy:
		if list_copy.count(j) >= 2:
			# printer.append(list_copy.index(j,b))
			print(str(j) + "의 인덱스 값은 " + str(list_copy.index(j,b))  + "입니다.")
			b = list_copy.index(j) + 1

	return printer



# print(anagram(['0952', '5239', '1270', '8581', '7458', '3414', '7906', '2356', '4360', '3491', '6232', '5927', '2735', '2509', '5849', '8457', '9340', '1858', '8602', '5784']))
anagram(['0952', '5239', '1270', '8581', '7458', '3414', '7906', '2356', '4360', '3491', '6232', '5927', '2735', '2509', '5849', '8457', '9340', '1858', '8602', '5784'])