import tamil
# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

sentence = "வலை, வானம், விலை, வீடு, வெள்ளி, வேம்பு, வையம், வௌவுதல், வேவ்வாறு ஏ ஐ ஓ யான், யாண்டு, யாறு, கொல்லாது"
# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.

உயிர்மெய்_முதலெழுத்து_வவரிசை=["வ", "வா", "வி", "வீ", "வெ", "வே", "வை", "வௌ"]

def uyirmei_va_check(word, உயிர்மெய்_முதலெழுத்து_வவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_வவரிசை:
	
	    return True
	else:
	    return False
	    
for word in sentence.split():
	print(word, uyirmei_va_check(word, உயிர்மெய்_முதலெழுத்து_வவரிசை))
	
# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
# வேவ்வாறு True > False
# இதுகுறித்த தெளிவு தேவை. இதற்குப் புதியதாக விதி எழுதுதல் வேண்டும்.

