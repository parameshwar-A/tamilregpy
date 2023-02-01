import tamil

# 1) ட் ற் ல் ள் + க ச ப
# ஒரு சொல்லில் ட், ற், ல், ள் ஆகிய எழுத்துக்களுக்குப் பின்பு ஆகிய க, ச, ப ஆகிய எழுத்துக்கள் மயங்கி வரும். எ-டு. கேட்க, கற்க, செல்க, கொள்க.

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)
Mei = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"]

if "ட்" in letters and letters.index("ட்")!=len(letters)-1:
	ind=letters.index("ட்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			print(True)
		else:
			print(False)

elif "ற்" in letters and letters.index("ற்")!=len(letters)-1:
	ind=letters.index("ற்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			print(True)
		else:
			print(False)

elif "ல்" in letters and letters.index("ல்")!=len(letters)-1:
	ind=letters.index("ல்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			print(True)
		else:
			print(False)

elif "ள்" in letters and letters.index("ள்")!=len(letters)-1:
	ind=letters.index("ள்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			print(True)
		else:
			print(False)
else:
		print(False)
