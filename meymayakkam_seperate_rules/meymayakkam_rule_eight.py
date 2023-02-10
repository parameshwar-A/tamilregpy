import tamil
# 	ஈரொற்றுடனிலை மெய்ம்மயக்கம்
#		ய், ர், ழ் + க ச த ப ங ஞ ந ம 
#		பாய்ச்சு, வாய்த்தது, வேய்ங்குழல், நாய்க்கடி
word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)
Mei = ["க்", "ச்", "த்", "ப்", "ங்", "ஞ்", "ந்", "ம்"]

if "ய்" in letters and letters.index("ய்")!=len(letters)-1:
	ind=letters.index("ய்")
	if letters[ind+1] in Mei:
		print (True)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ங்" or  root_last=="ஞ்" or root_last=="ந்" or  root_last=="ம்":
			print(True)
		else:
			print(False)
		
elif "ர்" in letters and letters.index("ர்")!=len(letters)-1:
	ind=letters.index("ர்")
	if letters[ind+1] in Mei:
		print (True)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ங்" or  root_last=="ஞ்" or root_last=="ந்" or  root_last=="ம்":
			print(True)
		else:
			print(False)

elif "ழ்" in letters and letters.index("ழ்")!=len(letters)-1:
	ind=letters.index("ழ்")
	if letters[ind+1] in Mei:
		print (True)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ங்" or  root_last=="ஞ்" or root_last=="ந்" or  root_last=="ம்":
			print(True)
		else:
			print(False)

#		Enter the sentence to check: நாய்க்கடி
#			False
#		Enter the sentence to check: வேய்ங்குழல்
#			True
#		Enter the sentence to check: நாய்க்கடி
#			True
#		Enter the sentence to check: பாய்ச்சு
#			True
#		Enter the sentence to check: வாய்த்தது
#			True
