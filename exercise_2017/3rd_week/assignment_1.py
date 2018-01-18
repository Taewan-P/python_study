def score_average():
	count = 0
	total = 0
	failed = 0
	while True:
		score = input()
		if score.isdigit():
			score = int(score)
			if score != 0:
				if score > 0 and score < 60:
					failed += 1
				elif score >= 60 and score <= 100:
					total += score
					count += 1
			else:
				break

	print(count)
	if count != 0:
		print(float(round(total/count,1)))
	
	if failed != 0:
		print(failed)

score_average()