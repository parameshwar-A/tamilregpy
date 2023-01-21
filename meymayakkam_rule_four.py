import tamil

# 4) ஞ் ந் ம் வ் + ய
# ஞ். ந், ம், வ் எழுத்துக்களுக்குப் பின்பு ய எழுத்து மயங்கி வரும். எ-டு. உரிஞ்யாது, தெவ்யாது.

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)

if "ஞ்" in letters and letters.index("ஞ்")!=len(letters)-1:
	ind=letters.index("ஞ்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ய்":
		print(True)
	else:
		print(False)

elif "ந்" in letters and letters.index("ந்")!=len(letters)-1:
	ind=letters.index("ந்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ய்":
		print(True)
	else:
		print(False)
		
elif "ம்" in letters and letters.index("ம்")!=len(letters)-1:
	ind=letters.index("ம்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ய்":
		print(True)
	else:
		print(False)
		
elif "வ்" in letters and letters.index("வ்")!=len(letters)-1:
	ind=letters.index("வ்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ய்":
		print(True)
	else:
		print(False)
