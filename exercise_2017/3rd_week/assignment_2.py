def isleapyear(year):
	if int(year) < 0:
		return 0
	return int(year)%4==0 and (int(year)%400==0 or int(year) %100 !=0) # 숫자 큰거부터 걸러내서 윤년을 찾는다.

# for x in range(2000,2020):
# 	print(x,isleapyear(x))

print(isleapyear(2100))