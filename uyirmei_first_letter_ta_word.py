import tamil
# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

sentence = "தத்தை, தாடி, திற்றி, தீமை, துணி, தூணி, தெற்றி, தேவர், தையல், தொண்டை, தோடு, தௌவை, தோவ்வாறு ஏ ஐ ஓ இவ்விடத்தில் சொல் சோறு கொல்லாது"
# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.

உயிர்மெய்_முதலெழுத்து_தவரிசை=["த", "தா", "தி", "தீ", "து", "தூ", "தெ", "தே", "தை", "தொ", "தோ", "தௌ"]

def uyirmei_ta_check(word, உயிர்மெய்_முதலெழுத்து_தவரிசை):
	first_letter=tamil.utf8.get_letters(word)[0]

	if first_letter in உயிர்மெய்_முதலெழுத்து_தவரிசை:
	
	    return True
	else:
	    return False
	    
for word in sentence.split():
	print(word, uyirmei_ta_check(word, உயிர்மெய்_முதலெழுத்து_தவரிசை))
	
# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
# தோவ்வாறு True > False
# இதுகுறித்த தெளிவு தேவை. இதற்குப் புதியதாக விதி எழுதுதல் வேண்டும்.

