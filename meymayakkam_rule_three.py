import tamil

# 3) ங் ஞ் ண் ந் ம் ன் + தத்தமிசைகள் (க ச ட த ப ற)
# மெல்லின எழுத்துக்கள் ஆகிய ங், ஞ், ண், ந், ம், ன் ஆகிய எழுத்துக்களுக்குப் பின்பு அதனுடைய ஒத்த ஒலிகளாக அறியப்படுகின்ற வல்லின எழுத்துக்கள் ஆகிய க, ச, ட, த, ப, ற ஆகிய எழுத்துகள் மயங்கி வரும். 
# இதனை அடிப்படையாக வைத்தே க்ங், ச்ஞ், ட்ண், த்ந், ப்ம், ற்ன் என்ற மெய் எழுத்து வரிசைமுறை தமிழ்மொழியில் இடம்பெறுகின்றன. 
# இதனை இப்படிப் புரிந்துகொள்ளலாம். ங் என்ற எழுத்தை அடுத்து க எழுத்து வரும். 
# அதுபோல் ஞ்ச, ண்ட, ந்த, ம்ப, ன்ற என்ற என்ற எழுத்துக்கள் மயங்கி வருவதை நாம் பார்க்கமுடியும். 
# எ-டு. மாங்காய், பிஞ்சு, மண்டை, வந்து, வம்பு, சென்ற.

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)

if "ங்" in letters and letters.index("ங்")!=len(letters)-1:
	ind=letters.index("ங்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="க்":
		print(True)
	else:
		print(False)
		
elif "ஞ்" in letters and letters.index("ஞ்")!=len(letters)-1:
	ind=letters.index("ஞ்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ச்":
		print(True)
	else:
		print(False)

elif "ண்" in letters and letters.index("ண்")!=len(letters)-1:
	ind=letters.index("ண்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ட்":
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
	if root_last=="த்":
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
	if root_last=="ப்":
		print(True)
	else:
		print(False)
		
elif "ன்" in letters and letters.index("ன்")!=len(letters)-1:
	ind=letters.index("ன்")
	root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	if type(root_words)==tuple:
		root_last=root_words[0]
	else:
		root_last=root_words
	if root_last=="ற்":
		print(True)
	else:
		print(False)
