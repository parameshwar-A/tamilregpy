import tamil

# 6) ய் ர் ழ் + க ச த ப ஞ ந ம ய வ ங
# ய், ர், ழ் ஆகிய எழுத்துக்களுக்குப் பின்பு க, ச, த, ப, ஞ, ந, ம, ய, வ, ங எழுத்துக்கள் மயங்கி வரும். 
# எ-டு. நாய்க்கடி, வாழ்க்கை, வேர்வை, வாழ்வு, வேய்ங்குழல்.

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)

if "ய்" in letters and letters.index("ய்")!=len(letters)-1:
	ind=letters.index("ய்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ஞ்" or  root_last=="ந்" or root_last=="ம்" or  root_last=="ய்" or root_last=="வ்"  or root_last=="ங்":
		print(True)
	else:
		print(False)
		
elif "ர்" in letters and letters.index("ர்")!=len(letters)-1:
	ind=letters.index("ர்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ஞ்" or  root_last=="ந்" or root_last=="ம்" or  root_last=="ய்" or root_last=="வ்"  or root_last=="ங்":
		print(True)
	else:
		print(False)

elif "ழ்" in letters and letters.index("ழ்")!=len(letters)-1:
	ind=letters.index("ழ்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ஞ்" or  root_last=="ந்" or root_last=="ம்" or  root_last=="ய்" or root_last=="வ்"  or root_last=="ங்":
		print(True)
	else:
		print(False)
