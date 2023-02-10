word_data={
"வினாவெழுத்து" : ["எ"] # சான்று :- எ+பொருள் = எப்பொருள்  # இங்கு விதி எழுத தங்களது உதவி தேவை?
}

sentence = "ஒரு அப்பொருள் அந்தாஅ இப்பொருள் மக்கள் ஏ கெடுப்பதூஉ மொழியாகவேஎ ஆ எப்பொருள் உவ் ஊ பொருந் அடிப்படையில் வெரிந் தமிழ் பதினெட்டாவது இடத்தில் உள்ளது."

def uyir_check(word, word_data):
	last_letter=word[0:]
	print(last_letter)
	for key, valuelist in word_data.items():
		if last_letter in valuelist:
			return True
	return False

for word in sentence.split():
	print(word, uyir_check(word,word_data))

# முடிபு
#ஒரு
#ஒரு False
#அப்பொருள்
#அப்பொருள் False
#அந்தாஅ
#அந்தாஅ False
#இப்பொருள்
#இப்பொருள் False
#மக்கள்
#மக்கள் False
#ஏ
#ஏ False
#கெடுப்பதூஉ
#கெடுப்பதூஉ False
#மொழியாகவேஎ
#மொழியாகவேஎ False
#ஆ
#ஆ False
#எப்பொருள்
#எப்பொருள் False > True 
#உவ்
#உவ் False
#ஊ
#ஊ False
#பொருந்
#பொருந் False
#அடிப்படையில்
#அடிப்படையில் False
#வெரிந்
#வெரிந் False
#தமிழ்
#தமிழ் False
#பதினெட்டாவது
#பதினெட்டாவது False
#இடத்தில்
#இடத்தில் False
#உள்ளது.
#உள்ளது. False
