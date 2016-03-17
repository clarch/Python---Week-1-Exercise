def num_to_word(num):
	words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	B = list(map(int, str(num)))
	for b in B:
		print words[b] + " "		

num_to_word(2345)