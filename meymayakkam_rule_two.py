import tamil

# 2) ல் ள் + ய வ
# ல், ள் ஆகிய எழுத்துக்களுக்குப் பின்பு ய, வ எழுத்துக்கள் மயங்கி வரும். எ-டு. கொல்யானை, வெள்வளை.

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)
Mei = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"]

if "ல்" in letters and letters.index("ல்")!=len(letters)-1:
	ind=letters.index("ல்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="ய்" or  root_last=="வ்":
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
		if root_last=="ய்" or  root_last=="வ்":
			print(True)
		else:
			print(False)
