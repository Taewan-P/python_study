def minsteps(n):
	memo = [0] * (n + 1) #memo[숫자] 에는 그 "숫자"를 구하는데 필요한 최소 횟수를 저장한 것이다...? 
	for i in range(1,n+1):
		if i>1: #이 if 문이 왜 들어가야 되는걸까??? ->i = 1 일때는 밑에 구문이 돌아가면 안되기 때문이다.
			memo[i] = 1 + memo[i-1]
			if i%2 == 0:
				memo[i] = min(memo[i], 1 + memo[i//2]) # 1 + memo 이거 왜 들어가는거지?
			if i%3 == 0:
				memo[i] = min(memo[i], 1 + memo[i//3])
	return memo[n]


def gugudan1():
	for dan in range(2,10):
		for i in range(2,10):
			if i == 6:
				print("")
			print(str(dan) + " x " + str(i) + " = " + str(dan*i).rjust(2), end = ' ' )
		print("\n")


def gugudan2():
	for num in range(2,10):
		for dan in range(2,6):
			print(str(dan) + " x " + str(num) + " = " + str(dan*num).rjust(2), end = ' ')
		print("")
	print("")
	for num in range(2,10):
		for dan in range(6,10):
			print(str(dan) + " x " + str(num) + " = " + str(dan*num).rjust(2), end = ' ')
		print("")



#TestCase
print(minsteps(1)) # 0
print(minsteps(2)) # 1
print(minsteps(4)) # 2
print(minsteps(7)) # 3
print(minsteps(11)) # 4
print(minsteps(17)) # 5
print(minsteps(23)) # 6
print(minsteps(237)) # 8
print(minsteps(317)) # 10
print(minsteps(514)) # 8
print(minsteps(717)) # 11
print(minsteps(1993)) # 11
gugudan1()
gugudan2()



