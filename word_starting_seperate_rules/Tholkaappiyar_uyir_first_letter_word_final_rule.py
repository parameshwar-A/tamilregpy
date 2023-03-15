import tamil
# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

sentence = "வலை, வானம், விலை, வீடு, வெள்ளி, வேம்பு, வையம், வௌவுதல், வேவ்வாறு ஏ ஐ ஓ யான், யாண்டு, யாறு, கொல்லாது"
# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.

உயிர்_முதலெழுத்து=["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
def uyirezhuthu_check(word, உயிர்_முதலெழுத்து):
	first_letter=tamil.utf8.get_letters(word)[0]
	
	if first_letter in உயிர்_முதலெழுத்து:
	
	    return True
	else:
	    return False

#இது உயிர் எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_கவரிசை=["க", "கா", "கி", "கீ", "கு", "கூ", "கெ", "கே", "கை", "கொ", "கோ", "கௌ"]

def uyirmei_ka_check(word, உயிர்மெய்_முதலெழுத்து_கவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_கவரிசை:
	
	    return True
	else:
	    return False

#இது கவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_சவரிசை=["ச", "சா", "சி", "சீ", "சு", "சூ", "செ", "சே", "சொ", "சோ"]

def uyirmei_sa_check(word, உயிர்மெய்_முதலெழுத்து_சவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_சவரிசை:
	
	    return True
	else:
	    return False

#இது சவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_ஞவரிசை=["ஞா", "ஞெ", "ஞொ"]

def uyirmei_nga_check(word, உயிர்மெய்_முதலெழுத்து_ஞவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_ஞவரிசை:
	
	    return True
	else:
	    return False

#இது ஞவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_தவரிசை=["த", "தா", "தி", "தீ", "து", "தூ", "தெ", "தே", "தை", "தொ", "தோ", "தௌ"]

def uyirmei_ta_check(word, உயிர்மெய்_முதலெழுத்து_தவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_தவரிசை:
	
	    return True
	else:
	    return False

#இது தவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_நவரிசை=["ந", "நா", "நி", "நீ", "நு", "நூ", "நெ", "நே", "நை", "நொ", "நோ", "நௌ"]

def uyirmei_na_check(word, உயிர்மெய்_முதலெழுத்து_நவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_நவரிசை:
	
	    return True
	else:
	    return False

#இது நவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_பவரிசை=["ப", "பா", "பி", "பீ", "பு", "பூ", "பெ", "பே", "பை", "பொ", "போ", "பௌ"]

def uyirmei_pa_check(word, உயிர்மெய்_முதலெழுத்து_பவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_பவரிசை:
	
	    return True
	else:
	    return False

#இது பவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_மவரிசை=["ம", "மா", "மி", "மீ", "மு", "மூ", "மெ", "மே", "மை", "மொ", "மோ", "மௌ"]

def uyirmei_ma_check(word, உயிர்மெய்_முதலெழுத்து_மவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_மவரிசை:
	
	    return True
	else:
	    return False

#இது மவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_யவரிசை=["யா"]

def uyirmei_ya_check(word, உயிர்மெய்_முதலெழுத்து_யவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_யவரிசை:
	
	    return True
	else:
	    return False

#இது யவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

உயிர்மெய்_முதலெழுத்து_வவரிசை=["வ", "வா", "வி", "வீ", "வெ", "வே", "வை", "வௌ"]

def uyirmei_va_check(word, உயிர்மெய்_முதலெழுத்து_வவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_வவரிசை:
	
	    return True
	else:
	    return False

#இது வவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.
	
# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
# வேவ்வாறு True > False
# இதுகுறித்த தெளிவு தேவை. இதற்குப் புதியதாக விதி எழுதுதல் வேண்டும்.

if uyirezhuthu_check or uyirmei_ka_check or uyirmei_sa_check or uyirmei_nga_check  or uyirmei_ta_check or uyirmei_na_check or uyirmei_pa_check or uyirmei_ma_check or uyirmei_ya_check or uyirmei_va_check:
	print (True)
else:
	print (false)

