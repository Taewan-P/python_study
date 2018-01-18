# 모범답안

##### 1 #####
# 삼각수 구하기

def trinum(n):
    if n >= 1:
        return n + trinum(n-1)
    else:
        return 0 

# 테스트 케이스
# print(trinum(1)) # 1
# print(trinum(3)) # 6
# print(trinum(6)) # 21
# print(trinum(11)) # 66
# print(trinum(0)) # 0
# print(trinum(-3)) # 0

def trinumT(n):
    def loop(n,r):
        if n >= 1:
            return loop(n-1,n+r)
        else:
            return r
    return loop(n,0)

# 테스트 케이스
# print(trinumT(1)) # 1
# print(trinumT(3)) # 6
# print(trinumT(6)) # 21
# print(trinumT(11)) # 66
# print(trinumT(0)) # 0
# print(trinumT(-3)) # 0

def trinumW(n):
    r = 0
    while n >= 1:
        r += n
        n -= 1
    return r

# 테스트 케이스
# print(trinumW(1)) # 1
# print(trinumW(3)) # 6
# print(trinumW(6)) # 21
# print(trinumW(11)) # 66
# print(trinumW(0)) # 0
# print(trinumW(-3)) # 0


##### 2 #####
# Palindrom
# def is_pal(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     else:
#         return is_pal(s[1:-1])

def is_pal(s):
    return len(s) <= 1 or s[0] == s[-1] and is_pal(s[1:-1])

# 테스트 케이스
# print(is_pal("")) # True
# print(is_pal("a")) # True
# print(is_pal("aa")) # True
# print(is_pal("aba")) # True
# print(is_pal("abba")) # True
# print(is_pal("aaba")) # False
# print(is_pal("abcba")) # True
# print(is_pal("여보 안경 안 보여")) # False
# print(is_pal("여보안경안보여")) # True


##### 3 #####
### A ###
# 표준입력창에서 주민등록번호의 앞 6자리를 입력받아서 생년월일을 년.월,일 정수투플로 내주는 함수

def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def is_valid_date(year,month,day):
    return year > 0 and 1 <= month <= 12 and \
           (month in [1,3,5,7,8,10,12] and 1 <= day <= 31 or 
            month in [4,6,9,11] and 1 <= day <= 30 or 
            is_leap_year(year) and 1 <= day <= 29 or 
            1 <= day <= 28) 

def get_valid_date_6():
    s = input('Type 6 digits: ')
    while not (s.isdigit() and len(s) == 6):
        s = input('Type 6 digits: ')
    year = int(s[:2])
    if year <= 17:
        year += 2000
    else:
        year += 1900
    month = int(s[2:4])
    day = int(s[4:])
    if is_valid_date(year,month,day):
        return (year,month,day)
    else:
        return None

# print(get_valid_date_6())

# 입력 테스트 케이스 
# 160425 # => (2016, 4, 25)
# 160431 # => None
# 160229 # => (2016, 2, 29)
# 170229 # => None


### B ###
# 표준입력창에서 주민등록번호의 앞 6자리를 입력받아서 생년월일을 년.월,일 정수투플로 내주는 함수

def next_month(year, month):
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)

def days_in_month(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month in [2]:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 0

def date_plus(year, month, day, days):
    days_left = days_in_month(year,month) - day
    if days_left < days:
        days -= days_left
        (year, month) = next_month(year, month)
        days_this_month = days_in_month(year, month)
        while days_this_month < days:
            days -= days_this_month
            (year, month) = next_month(year, month)
            days_this_month = days_in_month(year,month)
        return (year, month, days)
    else:
        return (year, month, day + days)

# 테스트 케이스     
# print(date_plus(2017,4,20,2)) # => (2017, 4, 22)
# print(date_plus(2017,4,20,7)) # => (2017, 4, 27)
# print(date_plus(2017,4,20,10)) # => (2017, 4, 30)
# print(date_plus(2017,4,20,11)) # => (2017, 5, 1)
# print(date_plus(2017,4,20,50)) # => (2017, 6, 9)
# print(date_plus(2017,4,20,100)) # => (2017, 7, 29)
# print(date_plus(2017,4,20,200)) # => (2017, 11, 6)
# print(date_plus(2017,4,20,300)) # => (2018, 2, 14)
# print(date_plus(2017,4,20,1000)) # => (2020, 1, 15)


##### 4 #####
# 문자열에서 특정 문자 모두 없애기

def remove(x,xs):
    if xs != "":
        if x != xs[0]:
            return xs[0] + remove(x,xs[1:])
        else:
            return remove(x,xs[1:])
    else:
        return ""

# 테스트 케이스
# print(remove('a','abracadabra'))
# print(remove('z','abracadabra'))

def removeT(x,xs):
    def loop(xs,rs):
        if xs != "":
            if x != xs[0]:
                return loop(xs[1:],rs+xs[0])
            else:
                return loop(xs[1:],rs)
        else:
            return rs
    return loop(xs,"")

# 테스트 케이스
# print(removeT('a','abracadabra'))
# print(removeT('z','abracadabra'))

def removeW(x,xs):
    rs = ""
    while xs != "":
        if x != xs[0]:
            rs += xs[0]
        xs = xs[1:]
    return rs

# 테스트 케이스
# print(removeW('a','abracadabra'))
# print(removeW('z','abracadabra'))


##### 5 #####
# 순열 permutation
# assume: n > 0, k > 0, n >= k
# 양수 인수만 제대로 처리하면 된다. 
# 즉, 인수가 양수인지는 함수 호출하기 전에 이미 확인했다고 가정한다. 
# 그리고  n < k 인 경우에는 0을 내주도록 해야 한다.

# def permutation0(n,k):
#     if k > 0:
#         return None # 여기에 적절한 식을 채워 넣자.
#     else:
#         return 1

# def permutation1(n,k):
#     pass # 꼬리 재귀

# def permutation2(n,k):
#     pass # while 문

# def permutation3(n,k):
#     pass # for 문

# print(permutation0(1,1)) # => 1
# print(permutation0(2,1)) # => 2
# print(permutation0(2,2)) # => 2
# print(permutation0(3,1)) # => 3
# print(permutation0(3,2)) # => 6
# print(permutation0(3,3)) # => 6
# print(permutation0(4,1)) # => 4
# print(permutation0(4,2)) # => 12
# print(permutation0(4,3)) # => 24
# print(permutation0(4,4)) # => 24

# print(permutation1(1,1)) # => 1
# print(permutation1(2,1)) # => 2
# print(permutation1(2,2)) # => 2
# print(permutation1(3,1)) # => 3
# print(permutation1(3,2)) # => 6
# print(permutation1(3,3)) # => 6
# print(permutation1(4,1)) # => 4
# print(permutation1(4,2)) # => 12
# print(permutation1(4,3)) # => 24
# print(permutation1(4,4)) # => 24

# print(permutation2(1,1)) # => 1
# print(permutation2(2,1)) # => 2
# print(permutation2(2,2)) # => 2
# print(permutation2(3,1)) # => 3
# print(permutation2(3,2)) # => 6
# print(permutation2(3,3)) # => 6
# print(permutation2(4,1)) # => 4
# print(permutation2(4,2)) # => 12
# print(permutation2(4,3)) # => 24
# print(permutation2(4,4)) # => 24

# print(permutation3(1,1)) # => 1
# print(permutation3(2,1)) # => 2
# print(permutation3(2,2)) # => 2
# print(permutation3(3,1)) # => 3
# print(permutation3(3,2)) # => 6
# print(permutation3(3,3)) # => 6
# print(permutation3(4,1)) # => 4
# print(permutation3(4,2)) # => 12
# print(permutation3(4,3)) # => 24
# print(permutation3(4,4)) # => 24

# version 1

def permutation(n,k):
    if k > 1:
        return n * permutation(n-1,k-1)
    else:
        return n

def permutation(n,k):
    # assume: n > 0, k > 0
    def loop(n,k,p):
        if k > 1:
            return loop(n-1,k-1,p*n)
        else:
            return p * n
    return loop(n,k,1)

def permutation(n,k):
    # assume: n > 0, k > 0
    p = 1
    while k > 1:
        p *= n
        n -= 1
        k -= 1
    return p * n

def permutation(n,k):
    p = 1
    for i in range(n,n-k,-1): # range(n-k+1,n+1)
        p *= i 
    return p 

# version 2 : This solution is better!!!

def permutation(n,k):
    if k > 0:
        return n * permutation(n-1,k-1)
    else:
        return 1

def permutation(n,k):
    # assume: n > 0, k > 0
    def loop(n,k,p):
        if k > 0:
            return loop(n-1,k-1,p*n)
        else:
            return p
    return loop(n,k,1)

def permutation(n,k):
    # assume: n > 0, k > 0
    p = 1
    while k > 0:
        p *= n
        n -= 1
        k -= 1
    return p

def permutation(n,k):
    p = 1
    for i in range(n,n-k,-1): # range(n-k+1,n+1)
        p *= i 
    return p 

# print(permutation(1,1)) # => 1
# print(permutation(2,1)) # => 2
# print(permutation(2,2)) # => 2
# print(permutation(3,1)) # => 3
# print(permutation(3,2)) # => 6
# print(permutation(3,3)) # => 6
# print(permutation(4,1)) # => 4
# print(permutation(4,2)) # => 12
# print(permutation(4,3)) # => 24
# print(permutation(4,4)) # => 24


##### 6 #####

def drop_before(s,index):
    if s != [] and index > 0:
        return drop_before(s[1:],index-1)
    else:
        return s

### A ###  
# def drop_before(s,index):
#     pass # while 문 버전

def drop_before(s,index):
    while s != [] and index > 0:
        s = s[1:]
        index -= 1
    return s

# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("drop_before(s,0) =", drop_before(s,0)) 
# print("drop_before(s,1) =", drop_before(s,1))
# print("drop_before(s,2) =", drop_before(s,2))
# print("drop_before(s,3) =", drop_before(s,3))
# print("drop_before(s,4) =", drop_before(s,4))
# print("drop_before(s,5) =", drop_before(s,5))
# print("drop_before(s,6) =", drop_before(s,6))
# print("drop_before(s,-3) =", drop_before(s,-3))
# print("drop_before([],4) =", drop_before([],4))

### B ###
# def take_before(s,index):
#     pass  # 재귀
 
# def take_before(s,index):
#     pass  # 꼬리 재귀

# def take_before(s,index):
#     pass  # while 문

def take_before(s,index):
    if s != [] and index > 0:
        return [s[0]] + take_before(s[1:],index-1)
    else:
        return []

def take_before(s,index):
    def loop(s,index,ss):
        if s != [] and index > 0:
            ss.append(s[0])
            return loop(s[1:],index-1,ss)
        else:
            return ss
    return loop(s,index,[])

def take_before(s,index):
    ss = []
    while s != [] and index > 0:
        ss.append(s[0])
        s = s[1:]
        index -= 1
    return ss


# s = [1,2,3,4,5]
# print("take_before(s,0) =", take_before(s,0))
# print("take_before(s,1) =", take_before(s,1))
# print("take_before(s,2) =", take_before(s,2))
# print("take_before(s,3) =", take_before(s,3))
# print("take_before(s,4) =", take_before(s,4))
# print("take_before(s,5) =", take_before(s,5))
# print("take_before(s,6) =", take_before(s,6))
# print("take_before([],4) =", take_before([],4))
# print("take_before(s,-3) =", take_before(s,-3))

### C ###
# def sublist(s,low,high):
#     if low < 0: low = 0
#     if high < 0: high = 0
#     if low <= high:
#         return None # 여기에 알맞은 식을 채워 넣자.
#     else:
#         return []

def sublist(s,low,high):
    if low < 0: low = 0
    if high < 0: high = 0
    if low <= high:
        return take_before(drop_before(s,low),high-low)
    else:
        return []

# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("sublist(s,0,0) => [] ?", sublist(s,0,0))
# print("sublist(s,0,1) => [1] ?", sublist(s,0,1))
# print("sublist(s,0,2) => [1, 2] ?", sublist(s,0,2))
# print("sublist(s,0,3) => [1, 2, 3] ?", sublist(s,0,3))
# print("sublist(s,0,4) => [1, 2, 3, 4] ?", sublist(s,0,4))
# print("sublist(s,0,5) => [1, 2, 3, 4, 5] ?", sublist(s,0,5))
# print("sublist(s,0,6) => [1, 2, 3, 4, 5] ?", sublist(s,0,6))
# print("sublist(s,1,1) => [] ?", sublist(s,1,1))
# print("sublist(s,1,2) => [2] ?", sublist(s,1,2))
# print("sublist(s,1,3) => [2, 3] ?", sublist(s,1,3))
# print("sublist(s,1,4) => [2, 3, 4] ?", sublist(s,1,4))
# print("sublist(s,1,5) => [2, 3, 4, 5] ?", sublist(s,1,5))
# print("sublist(s,1,6) => [2, 3, 4, 5] ?", sublist(s,1,6))
# print("sublist(s,2,2) => [] ?", sublist(s,2,2))
# print("sublist(s,2,3) => [3] ?", sublist(s,2,3))
# print("sublist(s,2,4) => [3, 4] ?", sublist(s,2,4))
# print("sublist(s,2,5) => [3, 4, 5] ?", sublist(s,2,5))
# print("sublist(s,2,6) => [3, 4, 5] ?", sublist(s,2,6))
# print("sublist(s,3,3) => [] ?", sublist(s,3,3))
# print("sublist(s,3,4) => [4] ?", sublist(s,3,4))
# print("sublist(s,3,5) => [4, 5] ?", sublist(s,3,5))
# print("sublist(s,3,6) => [4, 5] ?", sublist(s,3,6))
# print("sublist(s,5,2) => [] ?", sublist(s,5,2))
# print("sublist(s,-3,-2) => [] ?", sublist(s,-3,-2))


##### 7 #####
# 빈 숫자열("")은 함수 호출 전에 이미 확인했다고 가정하고 처리하지 않기로 한다.

def longest_streak0(s):
    contender = leader = s[0]
    streak_length = streak_record = 1 
    for n in s[1:]:
        if n == contender:
            streak_length += 1
        else:
            contender = n
            streak_length = 1
        if streak_length > streak_record:
            leader = contender
            streak_record = streak_length
    return (leader, streak_record)

# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak0(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0) 
# # => ('0', 3)
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1) 
# # => ('5', 4)
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2) 
# # => ('8', 2)
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3) 
# # => ('8', 3)

### A ###
# def longest_streak1(s):
#     contender = leader = s[0]
#     streak_length = streak_record = 1
#     contender_index = leader_index = 0
#     index = 1
#     for n in s[1:]:
#         pass # 이 부분을 채워 넣자.
#         index += 1
#     return leader, streak_record, leader_index

def longest_streak1(s):
    contender = leader = s[0]
    streak_length = streak_record = 1
    contender_index = leader_index = 0
    index = 1
    for n in s[1:]:
        if n == contender:
            streak_length += 1
        else:
            contender = n
            streak_length = 1
            contender_index = index
        if streak_length > streak_record:
            leader = contender
            streak_record = streak_length
            leader_index = contender_index 
        index += 1
    return leader, streak_record, leader_index

# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak1(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0) 
# # => ('0', 3, 15)
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1) 
# # => ('5', 4, 15)
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2) 
# # => ('8', 2, 19)
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3) 
# # => ('8', 3, 2)

### B ###
# def longest_streak2(s):
#     contender = leader = s[0]
#     streak_length = streak_record = 1
#     contender_index = leader_index = 0
#     ties = []
#     index = 1
#     for n in s[1:]:
#         pass # 이 부분을 채워 넣자.
#         index += 1
#     return [(leader, streak_record, leader_index)] + ties
    
def longest_streak2(s):
    contender = leader = s[0]
    streak_length = streak_record = 1
    contender_index = leader_index = 0
    ties = []
    index = 1
    for n in s[1:]:
        if n == contender:
            streak_length += 1
        else:
            contender = n
            streak_length = 1
            contender_index = index
        if streak_length > streak_record:
            leader = contender
            streak_record = streak_length
            leader_index = contender_index
            ties = []
        elif streak_length == streak_record:
            coleader = (contender,streak_length,contender_index)
            ties.append(coleader)
        index += 1
    return [(leader, streak_record, leader_index)] + ties

# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak2(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0) 
# # => [('0', 3, 15), ('1', 3, 44)]
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1) 
# # => [('5', 4, 15)]
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2) 
# # => [('8', 2, 19), ('2', 2, 25), ('8', 2, 45)]
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3) 
# # => [('8', 3, 2), ('7', 3, 14), ('1', 3, 18), ('0', 3, 23), ('9', 3, 26)]




