def split_digit(num): #4자리 수에서 각 자릿수를 나눠서 리스트에 담아주는 함수
	num.split()
	return [int(num[0]), int(num[1]), int(num[2]), int(num[3])]

def anagram(lists):
	list_sort = []
	j = 0
	count = 0
	#4자리 숫자를 한개씩 나눈후 정렬한 뒤에 2차원 
	#list_sort 는 입력받은 리스트의 각 자릿수를 정렬해서 넣어둔 리스트 ex) 4323 -> 2334

	for i in lists:
		a = split_digit(i)
		a.sort()
		list_sort.append(a)
	
	#비교 시작
	while True:
		if j == len(lists):
			break
		if list_sort.count(list_sort[j]) >= 2:
			k = list_sort[j]
			while k in list_sort:
				p = list_sort.index(k)
				print(lists[p],end = ' ') 
				list_sort.pop(p)
				lists.pop(p)

			print("")
		else: #애너그램이 아닐 경우
			j += 1
	return None


# anagram(['0952', '5239', '1270', '8581', '7458', '3414', '7906', '2356', '4360', '3491', '6232', '5927', '2735', '2509', '5849', '8457', '9340', '1858', '8602', '5784'])




