def minsteps0(n):
    if n > 1:
        r = 1 + minsteps0(n - 1)
        if n % 2 == 0:
            r = min(r, 1 + minsteps0(n // 2))
        if n % 3 == 0:
            r = min(r, 1 + minsteps0(n // 3))
        return r
    else:
        return 0

# print(minsteps0(1))
# print(minsteps0(2))
# print(minsteps0(3))
# print(minsteps0(4))
# print(minsteps0(7))
# print(minsteps0(10))
# print(minsteps0(23))
# print(minsteps0(237))
# print(minsteps0(317))
# print(minsteps0(514))

def minsteps1(n):
    memo = [0] * (n + 1)
    def loop(n):
        if n > 1:
            if memo[n] != 0:
                return memo[n]
            else:
                memo[n] = 1 + loop(n - 1) #자기보다 1작은 숫자의 min연산값 + 1
                if n % 2 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 2))
                if n % 3 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 3))
                return memo[n]
        else:
            return 0
    return loop(n)

# print(minsteps1(1))
# print(minsteps1(2))
# print(minsteps1(3))
# print(minsteps1(4))
# print(minsteps1(7))
print(minsteps1(10))
# print(minsteps1(23))
# print(minsteps1(237))
# print(minsteps1(317))
# print(minsteps1(514))
# print(minsteps1(997))
# print(minsteps1(998))

# def minsteps(n):
#     memo = [0] * (n + 1)
#     pass # for loop
#     return memo[n]

#print(minsteps(1)) # 0
#print(minsteps(2)) # 1
#print(minsteps(4)) # 2
#print(minsteps(7)) # 3
#print(minsteps(11)) # 4
#print(minsteps(17)) # 5
#print(minsteps(23)) # 6
#print(minsteps(237)) # 8
#print(minsteps(317)) # 10
#print(minsteps(514)) # 8
#print(minsteps(717)) # 11
#print(minsteps(1993)) # 11
