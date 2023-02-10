word_data={
"மெல்லின_மெய்" :  ["ஞ்", "ண்", "ந்", "ம்", "ன்"]
}

sentence = "ஒரு மொழியைத் தாய்மொழியாகக் கண் பேசும் மக்களின் உரிஞ் எண்ணிக்கை பொருந் அடிப்படையில் வெரிந் பதினெட்டாவது இடத்தில் உள்ளது."

def uyir_check(word, word_data):
	last_letter=word[-2:]
	print(last_letter)
	for key, valuelist in word_data.items():
		if last_letter in valuelist:
			return True
	return False

for word in sentence.split():
	print(word, uyir_check(word,word_data))
