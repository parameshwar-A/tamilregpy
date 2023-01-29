import tamil

# 1) ட் ற் ல் ள் + க ச ப
# ஒரு சொல்லில் ட், ற், ல், ள் ஆகிய எழுத்துக்களுக்குப் பின்பு ஆகிய க, ச, ப ஆகிய எழுத்துக்கள் மயங்கி வரும். எ-டு. கேட்க, கற்க, செல்க, கொள்க.

#word=input("Enter the word to check: ")

Mei = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"]
def meymayakkam1(word):
    letters=tamil.utf8.get_letters(word)
    if "ட்" in letters and letters.index("ட்")!=len(letters)-1:
	    ind=letters.index("ட்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			    return True
		    else:
			    return False

    elif "ற்" in letters and letters.index("ற்")!=len(letters)-1:
	    ind=letters.index("ற்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			    return True
		    else:
			    return False

    elif "ல்" in letters and letters.index("ல்")!=len(letters)-1:
	    ind=letters.index("ல்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			    return True
		    else:
			    return False

    elif "ள்" in letters and letters.index("ள்")!=len(letters)-1:
	    ind=letters.index("ள்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்" or  root_last=="ச்" or root_last=="ப்":
			    return True
		    else:
			    return False
    else:
		    return False
		    
# 2) ல் ள் + ய வ
# ல், ள் ஆகிய எழுத்துக்களுக்குப் பின்பு ய, வ எழுத்துக்கள் மயங்கி வரும். எ-டு. கொல்யானை, வெள்வளை.

def meymayakkam2(word):
    letters=tamil.utf8.get_letters(word)
    if "ல்" in letters and letters.index("ல்")!=len(letters)-1:
	    ind=letters.index("ல்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ய்" or  root_last=="வ்":
			    return True
		    else:
			    return False

    elif "ள்" in letters and letters.index("ள்")!=len(letters)-1:
	    ind=letters.index("ள்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ய்" or  root_last=="வ்":
			    return True
		    else:
			    return False
    else:
        return False

# 3) ங் ஞ் ண் ந் ம் ன் + தத்தமிசைகள் (க ச ட த ப ற)
# மெல்லின எழுத்துக்கள் ஆகிய ங், ஞ், ண், ந், ம், ன் ஆகிய எழுத்துக்களுக்குப் பின்பு அதனுடைய ஒத்த ஒலிகளாக அறியப்படுகின்ற வல்லின எழுத்துக்கள் ஆகிய க, ச, ட, த, ப, ற ஆகிய எழுத்துகள் மயங்கி வரும். 
# இதனை அடிப்படையாக வைத்தே க்ங், ச்ஞ், ட்ண், த்ந், ப்ம், ற்ன் என்ற மெய் எழுத்து வரிசைமுறை தமிழ்மொழியில் இடம்பெறுகின்றன. 
# இதனை இப்படிப் புரிந்துகொள்ளலாம். ங் என்ற எழுத்தை அடுத்து க எழுத்து வரும். 
# அதுபோல் ஞ்ச, ண்ட, ந்த, ம்ப, ன்ற என்ற என்ற எழுத்துக்கள் மயங்கி வருவதை நாம் பார்க்கமுடியும். 
# எ-டு. மாங்காய், பிஞ்சு, மண்டை, வந்து, வம்பு, சென்ற.

def meymayakkam3(word):
    letters=tamil.utf8.get_letters(word)
    if "ங்" in letters and letters.index("ங்")!=len(letters)-1:
	    ind=letters.index("ங்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்":
			    return True
		    else:
			    return False

		    
    elif "ஞ்" in letters and letters.index("ஞ்")!=len(letters)-1:
	    ind=letters.index("ஞ்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ச்":
			    return True
		    else:
			    return False

    elif "ண்" in letters and letters.index("ண்")!=len(letters)-1:
	    ind=letters.index("ண்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ட்":
			    return True
		    else:
			    return False
		    
    elif "ந்" in letters and letters.index("ந்")!=len(letters)-1:
	    ind=letters.index("ந்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="த்":
			    return True
		    else:
			    return False

    elif "ம்" in letters and letters.index("ம்")!=len(letters)-1:
	    ind=letters.index("ம்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ப்":
			    return True
		    else:
			    return False
		    
    elif "ன்" in letters and letters.index("ன்")!=len(letters)-1:
	    ind=letters.index("ன்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ற்":
			    return True
		    else:
			    return False
    else:
        return False
	    
			    
# 4) ஞ் ந் ம் வ் + ய
# ஞ். ந், ம், வ் எழுத்துக்களுக்குப் பின்பு ய எழுத்து மயங்கி வரும். எ-டு. உரிஞ்யாது, தெவ்யாது.


def meymayakkam4(word):
    letters=tamil.utf8.get_letters(word)
    if "ஞ்" in letters and letters.index("ஞ்")!=len(letters)-1:
	    ind=letters.index("ஞ்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ய்":
			    return True
		    else:
			    return False

    elif "ந்" in letters and letters.index("ந்")!=len(letters)-1:
	    ind=letters.index("ந்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ய்":
			    return True
		    else:
			    return False
		    
    elif "ம்" in letters and letters.index("ம்")!=len(letters)-1:
	    ind=letters.index("ம்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ய்":
			    return True
		    else:
			    return False
		    
    elif "வ்" in letters and letters.index("வ்")!=len(letters)-1:
	    ind=letters.index("வ்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="ய்":
			    return True
		    else:
			    return False
    else:
        return False
			    
# 5) ம் + வ
# ம் எழுத்துக்களுக்குப் பின்பு ய எழுத்து மயங்கி வருவதைப்போல் வ எழுத்தும் மயங்கி வரும். எ-டு. நிலம்வலிது.

def meymayakkam5(word):
    letters=tamil.utf8.get_letters(word)
    if "ம்" in letters and letters.index("ம்")!=len(letters)-1:
	    ind=letters.index("ம்")
	    if letters[ind+1] in Mei:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="வ்":
			    return True
		    else:
			    return False
    else:
        return False
		    
# 6) ய் ர் ழ் + க ச த ப ஞ ந ம ய வ ங
# ய், ர், ழ் ஆகிய எழுத்துக்களுக்குப் பின்பு க, ச, த, ப, ஞ, ந, ம, ய, வ, ங எழுத்துக்கள் மயங்கி வரும். 
# எ-டு. நாய்க்கடி, வாழ்க்கை, வேர்வை, வாழ்வு, வேய்ங்குழல்.
# விதி திஉத்தம் பெறல் வேண்டும்.
# Enter the sentence to check: நாய்க்கடி - True
# Enter the sentence to check: நாய்ங்கடி - True -> False
# Enter the sentence to check: வேய்ங்குழல் - True


Mei1 = ["ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"]
Mei2 = ["ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"]

def meymayakkam6(word):
    letters=tamil.utf8.get_letters(word)
    if "ய்" in letters and letters.index("ய்")!=len(letters)-1:
	    ind=letters.index("ய்")
	    if letters[ind+1] in Mei1:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ஞ்" or  root_last=="ந்" or root_last=="ம்" or  root_last=="ய்" or root_last=="வ்"  or root_last=="ங்":
			    return True
		    else:
			    return False
		    
    elif "ர்" in letters and letters.index("ர்")!=len(letters)-1:
	    ind=letters.index("ர்")
	    if letters[ind+1] in Mei2:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ஞ்" or  root_last=="ந்" or root_last=="ம்" or  root_last=="ய்" or root_last=="வ்"  or root_last=="ங்":
			    return True
		    else:
			    return False

    elif "ழ்" in letters and letters.index("ழ்")!=len(letters)-1:
	    ind=letters.index("ழ்")
	    if letters[ind+1] in Mei2:
		    return False
	    else:
		    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		    if type(root_words)==tuple:
			    root_last=root_words[0]
		    else:
			    root_last=root_words
		    if root_last=="க்" or  root_last=="ச்" or  root_last=="த்" or root_last=="ப்" or root_last=="ஞ்" or  root_last=="ந்" or root_last=="ம்" or  root_last=="ய்" or root_last=="வ்"  or root_last=="ங்":
			    return True
		    else:
			    return False
    else:
        return False
			    
# 7) ர ழ அலங்கடை
# ர, ழ என்ற எழுத்துக்கள் தவிர பிற எழுத்துக்கள் தன் எழுத்துக்களோடு தன் எழுத்துக்கள் மயங்கி வரும். 
# எ-டு. வாக்கு, இங்ஙனம், செஞ்ஞாயிறு, பச்சை, அட்டை, அண்ணன், அண்ணி

def meymayakkam7(word):
    letters=tamil.utf8.get_letters(word)
    if "ர்" in letters and letters.index("ர்")!=len(letters)-1:
	    ind=letters.index("ர்")
	    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	    if type(root_words)==tuple:
		    root_last=root_words[0]
	    else:
		    root_last=root_words
	    if root_last=="ர்":
		    return False
	    else:
		    return True

    elif "ழ்" in letters and letters.index("ழ்")!=len(letters)-1:
	    ind=letters.index("ழ்")
	    root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
	    if type(root_words)==tuple:
		    root_last=root_words[0]
	    else:
		    root_last=root_words
	    if root_last:="ழ்":
		    return False
	    else:
		    return True
    else:
        return False
