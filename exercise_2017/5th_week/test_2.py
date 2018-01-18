

###################
#      수정 X      #
# 곱셈 함수 보조 함수 #
def double(n):    #
  return n * 2    #
                  #
def halve(n):     #
  return n // 2   #
###################

def russianmult2(m,n):
    def loop(m,n,ans):
        if (n%2 == 0):
            return loop(double(m),halve(n),ans)
        elif n == 1:
            return m+ans
        else:
            return loop(double(m),halve(n),m+ans)

print(russianmult2(57,86))

def mult(m,n) : #러시아농부곱셈법 꼬리재귀함수
    def loop(m,n,ans) : #루프 함수
        if n%2 ==0 :
            return loop(m*2,n//2,ans)
        elif n == 1 :
            return ans + m
        else :
            return loop(m*2,n//2,ans+m) 
                
    if n == 0 :
        return 0
    else :
        return loop(m,n,0) #안전코딩?

# print(mult(57,86))





