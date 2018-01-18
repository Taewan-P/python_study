# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def get_number():
	return input("수를 입력하세요.\n")

def print_result(srm,res):
	print(srm,"의 제곱근은",res,"입니다.")


def isfloat(s):
	(m,_,n) = s.partition(".")
	return m.isdigit() and (n.isdigit() or n=="") or \
				 m == "" and n.isdigit()
				 #여기서 리턴뒤에 있는 문장을 실행하면 참 또는 거짓으로 출력된다!
	
	
def stop():
	cont = input('계속하시겠습니까? (y/n)')
	while not (cont == 'y' or cont == 'n'):
		cont = input('계속하시겠습니까? (y/n)')
	return cont == 'n' #리턴 뒤에 cont 가 n 이면 True 값을 리턴해주고, 아니면 False를 반환하기 때문에 38번줄 참조 

def safe_sqrt():
	import math
	print("제곱근을 구해드립니다.")
	print("0이상의 수를 입력하세요.")
	while True:
		srm = get_number()
		
		if not isfloat(srm):
			srm=get_number()
			while not isfloat(srm): #while 뒤에 not isfloat이 참이면 밑에줄을 실행 -> 실수(isfloat)가 아니기(not) 떄문에 실행하는거다.
				srm=get_number()
			
		res = math.sqrt(float(srm))
		print_result(srm,round(res,4))
		if stop(): #stop함수가 참 또는 거짓으로 나오는데 if문은 주어진 문장이 참이면 그밑의 줄을 실행한다.
			break #if 주어진 문장 \n 조건문 이면 주어진 문장을 실행한다.
	
	
	print("안녕히 가세요.")
	

safe_sqrt()