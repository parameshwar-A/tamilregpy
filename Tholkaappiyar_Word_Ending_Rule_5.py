word_data={
"ஓரெழுத்தொருமொழி" :  ["ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ"]
}

sentence = "ஒரு மொழியைத் அந்தாஅ தாயீஇ மக்கள் ஏ கெடுப்பதூஉ மொழியாகவேஎ ஆ கண் பேசும் ஓ மக்களோஒ ஈ உரிஞ் எண்ணிக்கை உவ் ஊ பொருந் அடிப்படையில் வெரிந் தமிழ் பதினெட்டாவது இடத்தில் உள்ளது."

def uyir_check(word, word_data):
	last_letter=word[-1:]
	print(last_letter)
	for key, valuelist in word_data.items():
		if last_letter in valuelist:
			return True
	return False

for word in sentence.split():
	print(word, uyir_check(word,word_data))
