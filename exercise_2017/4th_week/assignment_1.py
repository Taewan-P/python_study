# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 그냥 부호 지우는 프로그램

def remove_sign(s):
	if (s[0] == '+' ) \
	or (s[0] == '-' ):
		return s[1:]
	else:
		return s
	

def get_int_signed(message):
	s = input(message)
	while not (remove_sign(s).isdigit()):
		s = input(message)
	return int(s)


print(get_int_signed("정수를 입력하시오"))