import tamil
# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

sentence = "அவன் ஒரூஉ அங்கு இவ்வாறு பேசும் ஆ ஈ ஊ ஏ ஐ ஓ இவ்விடத்தில் உள்ளது"
# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.

uyir_list=["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
def uyir_check(word, uyir_list):
	last_letter=tamil.utf8.get_letters(word)[-1]
	root_words=tamil.utf8.splitMeiUyir(last_letter)
	if type(root_words)==tuple:
	    root_last=root_words[-1]
	else:
	    root_last=root_words
	if root_last in uyir_list:
	    return True
	else:
	    return False
	    
def uyir_check(word):
    uyir_list=["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
    last_letter=tamil.utf8.get_letters(word)[-1]
    root_words=tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words)==tuple:
        root_last=root_words[-1]
    else:
        root_last=root_words
    if root_last in uyir_list:
        return True
    else:
        return False

# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

mellinam_list=["ஞ்", "ண்", "ந்", "ம்", "ன்"]
def mellinam_check(word, mellinam_list):
	last_letter=tamil.utf8.get_letters(word)[-1]
	root_words=tamil.utf8.splitMeiUyir(last_letter)
	if type(root_words)==tuple:
	    root_last=root_words[-1]
	else:
	    root_last=root_words
	if root_last in mellinam_list:
	    return True
	else:
	    return False

def mellinam_check(word):
    mellinam_list=["ஞ்", "ண்", "ந்", "ம்", "ன்"]
    last_letter=tamil.utf8.get_letters(word)[-1]
    root_words=tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words)==tuple:
        root_last=root_words[-1]
    else:
        root_last=root_words
    if root_last in mellinam_list:
        return True
    else:
        return False

# இது மெல்லின எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

idaiyinam_list=["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"]
def idaiyinam_check(word, idaiyinam_list):
	last_letter=tamil.utf8.get_letters(word)[-1]
	root_words=tamil.utf8.splitMeiUyir(last_letter)
	if type(root_words)==tuple:
	    root_last=root_words[-1]
	else:
	    root_last=root_words
	if root_last in idaiyinam_list:
	    return True
	else:
	    return False

def idaiyinam_check(word):
    idaiyinam_list=["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"]
    last_letter=tamil.utf8.get_letters(word)[-1]
    root_words=tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words)==tuple:
        root_last=root_words[-1]
    else:
        root_last=root_words
    if root_last in idaiyinam_list:
        return True
    else:
        return False

# இது இடையின எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

oorezhuthoorumozhi_list=["ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ"]
def oorezhuthoorumozhi_check(word, oorezhuthoorumozhi_list):
	last_letter=tamil.utf8.get_letters(word)[-1]
	root_words=tamil.utf8.splitMeiUyir(last_letter)
	if type(root_words)==tuple:
	    root_last=root_words[-1]
	else:
	    root_last=root_words
	if root_last in oorezhuthoorumozhi_list:
	    return True
	else:
	    return False

def oorezhuthoorumozhi_check(word):
    oorezhuthoorumozhi_list=["ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ"]
    last_letter=tamil.utf8.get_letters(word)[-1]
    root_words=tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words)==tuple:
        root_last=root_words[-1]
    else:
        root_last=root_words
    if root_last in oorezhuthoorumozhi_list:
        return True
    else:
        return False

# இது ஓரெழுத்தொரு மொழி எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

alapedai_list=["அ", "இ", "உ", "எ", "ஒ"]
def alapedai_check(word, alapedai_list):
	last_letter=tamil.utf8.get_letters(word)[-1]

	if last_letter in alapedai_list:

	    return True
	else:
	    return False
def alapedai_check(word):
    alapedai_list=["அ", "இ", "உ", "எ", "ஒ"]
    last_letter=tamil.utf8.get_letters(word)[-1]
    if last_letter in alapedai_list:

        return True
    else:
        return False

# இது அளபெடை எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

suttu_list=["அ", "இ", "உ"]
vallinam_list=["க்", "ச்", "த்", "ப்", "வ்"]
def suttu_check(word, suttu_list, vallinam_list):
	first_letter=tamil.utf8.get_letters(word)[0]
	second_letter=tamil.utf8.get_letters(word)[1]

	if first_letter in suttu_list and second_letter in vallinam_list:
	    return True
	else:
	    return False
def suttu_check(word):
    suttu_list=["அ", "இ", "உ"]
    vallinam_list=["க்", "ச்", "த்", "ப்", "வ்"]
    first_letter=tamil.utf8.get_letters(word)[0]
    second_letter=tamil.utf8.get_letters(word)[1]

    if first_letter in suttu_list and second_letter in vallinam_list:
        return True
    else:
        return False

# இது சுட்டு எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

vallinam_list=["க்", "ச்", "த்", "ப்", "வ்", "ங்", "ந்"]
def vinaa_check(word, vallinam_list):
	if len(word)<2:
		return False
	first_letter=tamil.utf8.get_letters(word)[0]
	second_letter=tamil.utf8.get_letters(word)[1]

	if first_letter == "எ" and second_letter in vallinam_list:
	    return True
	else:
		return False

def vinaa_check(word):
    vallinam_list=["க்", "ச்", "த்", "ப்", "வ்", "ங்", "ந்"]
    if len(word)<2:
	    return False
    first_letter=tamil.utf8.get_letters(word)[0]
    second_letter=tamil.utf8.get_letters(word)[1]

# இது வினா எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
    if first_letter == "எ" and second_letter in vallinam_list:
        return True
    else:
        return False

if uyir_check or mellinam_check or idaiyinam_check or oorezhuthoorumozhi_check or alapedai_check or suttu_check or vinaa_check:
	print (True)
# இது வினா எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
#sentence = "அவன் ஒரூஉ அங்கு இவ்வாறு பேசும் ஆ ஈ ஊ ஏ ஐ ஓ இவ்விடத்தில் உள்ளது"
#sentence = "வணக்கம் நான் இப்பொது என்ன செய்யவேண்டும் "
#sentence = "வணக்கம் நான் அக்சிட்ஜபிக்ஜ்கச்டபிக்  என்ன செய்யவேண்டும் " -- This sentence has a wrong word but still we are getting correct only Kindly check on this
sentence = input("Enter the tamil sentence: ") # Will get sentence input from user prompt in terminal
issue_flag=False # This is the flag used to identify the issue
for word in sentence.split():
    if uyir_check(word) or mellinam_check(word) or idaiyinam_check(word) or oorezhuthoorumozhi_check(word) or alapedai_check(word) or suttu_check(word) or vinaa_check(word):
        print (True)
        continue

    else:
        issue_flag=True # When it finds a issue, it will change to True
        break
	    #print (false)

# If a issue is found it will print wrong word
if issue_flag:
    print("The sentence has a wrong word")
else:
	print (false)

print("All the words in the sentence are perfectly correct")
# இது இறுதியாக அனைத்து விதிகளையும் பொருத்திப் பார்த்து பதில் அளிப்பதற்குரிய நிரலாகும்.
