#결과 출력해주는 함수

def __print_result():
	import os
	os.system('cat result.txt')


#실습 1번
def find_last(filename, key):
	infile = open(filename, "r")
	outfile = open("result.txt", "w")
	
	s= infile.read()
	pos = s.rfind(key)
	if pos == -1:
		outfile.write(key + " is not found\n")
	else:
		outfile.write(key + " is found at" + str(pos) + "\n")
	
	infile.close()
	outfile.close()

#실습 2번
def find_all(filename, key):
	infile = open(filename, "r")
	outfile = open("result.txt", "w")
	s = infile.read()
	i = 0
	pos = s.find(key)
	if pos == -1:
		outfile.write(key +" is not found\n")
	else:
		while pos != -1:
			pos = s.find(key,pos+i) # (1+i) 번째의 단어
			if pos < 0:
				break
			outfile.write(key + "의 위치번호는 " + str(pos) + "\n")
			i += 1
			

	infile.close()
	outfile.close()


#실습 3번
def find_all_count(filename,key):
	infile = open(filename, "r")
	outfile = open("result.txt", "w")
	s = infile.read()
	num = 0
	pos = s.find(key)
	if pos == -1:
		outfile.write(key +" is not found\n")
		outfile.write("총 0번 등장\n")
	else:
		outfile.write(key + "의 위치번호는 " + str(pos) + "\n")
		num +=1
		while pos != -1:
			pos = s.find(key,pos+1)
			if pos < 0:
				break
			outfile.write(key + "의 위치번호는 " + str(pos) + "\n")
			num += 1
		outfile.write("총 " + str(num) + "번 등장\n")
			

	infile.close()
	outfile.close()


#실습 4번 (for 문 권장)
def one_sentence_per_line(filename):
	infile = open(filename,"r")
	outfile = open("result.txt", "w")
	text = infile.read()
	count = 0
	for i in text:
		if(i == '.' or i == '?' or i == '!'):
			outfile.write("\n\n")
			count += 1
		else:
			outfile.write(i)
	
	outfile.write("문장이 총 " + str(count) + "개\n")
	outfile.close()
	infile.close()
	print("done")


#실습 5번
def find_all_sentence(filename,key):
   infile = open(filename,"r")
   outfile = open("result.txt","w")
   outfile1 = open("temp.txt", "w+")
   text = infile.read()
   cnt = 0 # 단어가 나오는 문장의 갯수
   total_key = 0 # 총 나오는 단어의 갯수 
   num = 0 # 한 문장에서 나오는 단어의 갯수
   

   #임시 텍스트 파일 작성(한줄에 한문장씩 나오게끔.)
   for i in text:
      if(i == '.' or i == '?' or i == '!'):
         outfile1.write(i+"\n")
      else:
         outfile1.write(i)
   outfile1.close()
   outfile1 = open("temp.txt", "r")
   line = outfile1.readline()
   
   
   #한문장씩 키워드가 있는지 찾기 시작!
   while line!="":
      num = line.count(key)
      total_key += num
      if num != 0:
         outfile.write(key + "이(가) " + str(num) + "번 등장\n")
         outfile.write(line + "\n")
         cnt+=1
      line = outfile1.readline()
   outfile.write(key + "이(가) " + str(cnt) + "개 문장에서 " + str(total_key) + "번 등장\n")
   outfile.close()
   infile.close()
   outfile1.close()
   print("done")






#실습 1번 테스트

find_last("article.txt", "컴퓨터")
__print_result()
find_last("article.txt", "데스크탑")
__print_result()
find_last("article.txt", "한양대")
__print_result()

print("ㅡㅡㅡㅡㅡㅡㅡ")
#실습 2번 테스트

find_all("article.txt", "컴퓨터")
__print_result()
find_all("article.txt", "데스크탑")
__print_result()
find_all("article.txt", "한양대")
__print_result()

print("ㅡㅡㅡㅡㅡㅡ")
#실습 3번 테스트

find_all_count("article.txt", "컴퓨터")
__print_result()
find_all_count("article.txt", "데스크탑")
__print_result()
find_all_count("article.txt", "한양대")
__print_result()


#실습 4번 테스트

one_sentence_per_line("article.txt")
__print_result()


#실습 5번 테스트

find_all_sentence("article.txt", "컴퓨터")
__print_result()


