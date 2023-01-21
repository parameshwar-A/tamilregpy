import tamil

# 5) ம் + வ
# ம் எழுத்துக்களுக்குப் பின்பு ய எழுத்து மயங்கி வருவதைப்போல் வ எழுத்தும் மயங்கி வரும். எ-டு. நிலம்வலிது.

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)

if "ம்" in letters and letters.index("ம்")!=len(letters)-1:
	ind=letters.index("ம்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="வ்":
		print(True)
	else:
		print(False)
		
