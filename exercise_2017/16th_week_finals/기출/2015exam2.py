# 문제#2 - countnumber
def countnumber(xss):
    counter = 0
    pass
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
    pass

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
    pass
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
    pass

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

# 문제 #6: 순열 (난이도 높음)
def perm(xs):
    pass

# 테스트케이스
#xs0 = []
#xs1 = [1]
#xs2 = [1,2]
#xs3 = [1,2,3]
#xs4 = [1,2,3,4]
#print(perm(xs0))
#print(perm(xs1))
#print(perm(xs2))
#print(perm(xs3))
#print(perm(xs4))


# 문제#7: digit frequencies
def digit_freq(s):
    freqs = [0,0,0,0,0,0,0,0,0,0]
    pass
    dfreqs = []
    pass
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
    

