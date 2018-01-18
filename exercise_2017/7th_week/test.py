def __print_result():
	import os
	os.system('cat result.txt')


def find_all_sentence(filename,key):
	infile = open(filename,"r")
	outfile = open("result.txt","w")
	outfile1 = open("temp.txt", "w+")
	text = infile.read()
	count = 0 # 단어가 나오는 문장의 갯수
	total_key = 0 # 총 나오는 단어의 갯수 
	num = 0 # 한 문장에서 나오는 단어의 갯수 
	for i in text:
		if(i == '.' or i == '?' or i == '!'):
			outfile1.write("\n")
			line = outfile1.readline()
			num = line.count(key)
			total_key += num
			if num != 0:
				outfile.write(key + "이(가) " + str(num) + "번 등장\n")
				outfile.write(line)
				count += 1
		else:
			outfile1.write(i)
	
	outfile.write(key + "이(가) " + str(count) + "개 문장에서 " + str(total_key) + "번 등장")
	outfile.close()
	infile.close()
	outfile1.close()
	print("done")





find_all_sentence("article.txt", "컴퓨터")
__print_result()
find_all_sentence("article.txt", "데스크탑")
__print_result()
find_all_sentence("article.txt", "한양대")
__print_result()


