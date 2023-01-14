import tamil

word=input("Enter the word to check: ")
letters=tamil.utf8.get_letters(word)
if "ட்" in letters and letters.index("ட்")!=len(letters)-1:
	ind=letters.index("ட்")
	if letters[ind+1]=="க" or  letters[ind+1]=="ச" or letters[ind+1]=="ப":
		print(True)
	else:
		print(False)
elif "ற்" in letters and letters.index("ற்")!=len(letters)-1:
	ind=letters.index("ற்")
	if letters[ind+1]=="க" or  letters[ind+1]=="ச" or letters[ind+1]=="ப":
		print(True)
	else:
		print(False)
elif "ல்" in letters and letters.index("ல்")!=len(letters)-1:
	ind=letters.index("ல்")
	if letters[ind+1]=="க" or  letters[ind+1]=="ச" or letters[ind+1]=="ப":
		print(True)
	else:
		print(False)
elif "ள்" in letters and letters.index("ள்")!=len(letters)-1:
	ind=letters.index("ள்")
	if letters[ind+1]=="க" or  letters[ind+1]=="ச" or letters[ind+1]=="ப":
		print(True)
	else:
		print(False)
else:
	print(False)
