# 문제#2 - countnumber
def countnumber(xss):
    counter = 0
    for x in xss:
        if isinstance(x,list):
            counter += countnumber(x)
        else:
            counter += 1
    return counter

# 테스트케이스
#print(countnumber([1,2,3]))
#print(countnumber([1,[],3]))
#print(countnumber([1,[1,2,[3,4]]]))
#print(countnumber([[[[[[[[1,2,3]]]]]]]]))
#print(countnumber([]))
#print(countnumber([[[[3]],[4]],5,6,[7]]))
#print(countnumber([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]]))

# 답
# 3
# 2
# 5
# 3
# 0
# 5
# 14

# 문제 #3: 정방행렬 검사
def issquare(mat):
    if isinstance(mat,list):
        size = len(mat)
        for i in range(size):
            if not (isinstance(mat[i],list) and len(mat[i]) == size):
                return False
        return True
    else:
        return False

#print(issquare([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])) 
#print(issquare([])) 
#print(issquare([[]])) 
#print(issquare([[1]])) 
#print(issquare([[1,1],[1]])) 
#print(issquare([[1,1],[1,1]])) 

# 답
# True
# True
# False
# True
# False
# True

# 문제 #4: 정방행렬 - 전치
def transpose(sqmat):
    size = len(sqmat)
    transposed = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            transposed[i][j] = sqmat[j][i]
    return transposed

# 테스트케이스
#xs0 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#xs1 = [[0, -3, 6, 4], [3, 0, -9, 8], [-6, 9, 0, 2], [-4, -8, -2, 0]]
#print(transpose(xs0))
#print(transpose(xs1))

# 답
# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
# [[0, 3, -6, -4], [-3, 0, 9, -8], [6, -9, 0, -2], [4, 8, 2, 0]]

# 문제 #5: 정방행렬 - 반대칭행렬 검사
def antisymmetric(sqmat):
    size = len(sqmat)
    for i in range(size):
        for j in range(i,size):
            if sqmat[i][j] != -sqmat[j][i]:
                return False
    return True

# 테스트케이스
#xs0 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#xs1 = [[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]]
#xs2 = [[0,-3,6,4],[3,0,-9,8],[-6,9,0,2],[-4,-8,-2,0]]
#print(antisymmetric(xs0))
#print(antisymmetric(xs1))
#print(antisymmetric(xs2))

# 답
# False
# False
# True

# 문제 #6: 순열
def spread(xs):
    zs = []
    for x in xs:
        ys = xs[:]
        ys.remove(x)
        zs.append((x,ys))
    return zs

def mapcons(x,xss):
    rs = []
    for xs in xss:
        xs = [x] + xs
        rs.append(xs)
    return rs

def perms(xs):
    if len(xs) <= 1:
        return [xs]
    else:
        ps = []
        for (head,rest) in spread(xs):
            ps += mapcons(head,perms(rest))
        return ps

#print(perms([]))
#print(perms([1]))
#print(perms([1,2]))
#print(perms([1,2,3]))
#print(perms([1,2,3,4]))
        

# 문제#8: digit frequencies
def digit_freq(s):
    freqs = [0,0,0,0,0,0,0,0,0,0]
    for c in s:
        freqs[int(c)] += 1
    dfreqs = []
    for i in range(10):
        dfreqs.append((str(i),freqs[i]))
    dfreqs.sort(key=lambda t: t[1],reverse=True)
    return dfreqs

# 테스트케이스
#print(digit_freq(""))
#print(digit_freq("0987654321"))
#print(digit_freq("30774378274672034827764362738473"))

# 답
# [('0', 0), ('1', 0), ('2', 0), ('3', 0), ('4', 0),
#  ('5', 0), ('6', 0), ('7', 0), ('8', 0), ('9', 0)]
# [('0', 1), ('1', 1), ('2', 1), ('3', 1), ('4', 1),
#  ('5', 1), ('6', 1), ('7', 1), ('8', 1), ('9', 1)]
# [('7', 9), ('3', 6), ('4', 5), ('2', 4), ('6', 3),
#  ('8', 3), ('0', 2), ('1', 0), ('5', 0), ('9', 0)]
    
