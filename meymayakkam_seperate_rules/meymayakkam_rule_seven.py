import tamil

# 7) ர ழ அலங்கடை
# ர, ழ என்ற எழுத்துக்கள் தவிர பிற எழுத்துக்கள் தன் எழுத்துக்களோடு தன் எழுத்துக்கள் மயங்கி வரும். 
# எ-டு. வாக்கு, இங்ஙனம், செஞ்ஞாயிறு, பச்சை, அட்டை, அண்ணன், அண்ணி

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)

if "ர்" in letters and letters.index("ர்")!=len(letters)-1:
	ind=letters.index("ர்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ர்":
		print(False)
	else:
		print(True)

elif "ழ்" in letters and letters.index("ழ்")!=len(letters)-1:
	ind=letters.index("ழ்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last:="ழ்":
		print(False)
	else:
		print(True)
