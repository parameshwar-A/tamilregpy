import tamil
# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

sentence = "ஞாலம், ஞெகிழி, ஞொள்கிற்று, ஞாவ்வாறு ஏ ஐ ஓ இவ்விடத்தில் சொல் சோறு கொல்லாது"
# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.

உயிர்மெய்_முதலெழுத்து_ஞவரிசை=["ஞா", "ஞெ", "ஞொ"]

def uyirmei_nga_check(word, உயிர்மெய்_முதலெழுத்து_ஞவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_ஞவரிசை:
	
	    return True
	else:
	    return False
	    
for word in sentence.split():
	print(word, uyirmei_nga_check(word, உயிர்மெய்_முதலெழுத்து_ஞவரிசை))
	
# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
# ஞாவ்வாறு  True > False
# இதுகுறித்த தெளிவு தேவை. இதற்குப் புதியதாக விதி எழுதுதல் வேண்டும்.

