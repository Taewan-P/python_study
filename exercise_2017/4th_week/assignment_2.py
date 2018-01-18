# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def isfloat(s): #실수여부 확인?
	(m,_,n) = s.partition(".")
	return (m.isdigit() and (n.isdigit() or n=="")) or m=="" and n.isdigit()

def get_float(message):
	s = input(message)
	while not (s.isdigit() or isfloat(s)):
		s = input(message)
	return float(s)

def remove_sign(s):
	if (s[0] == '+' ) \
	 or (s[0] == '-' ):
		return s[1:]
	else:
		return s
	
def get_fixed_signed(message):
	s = input(message)
	while not (isfloat(remove_sign(s))): #일딴 부호는 지워보고 실수여부를 확인하자 
		s = input(message)
	return float(s)


print(get_fixed_signed("실수를 입력하시오"))