import tamil
# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

sentence = "அவன் ஒரூஉ அங்கு இவ்வாறு பேசும் ஆ ஈ ஊ ஏ ஐ ஓ இவ்விடத்தில் உள்ளது"
# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.

உயிர்_முதலெழுத்து=["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
def uyir_check(word, உயிர்_முதலெழுத்து):
	first_letter=tamil.utf8.get_letters(word)[0]
	root_words=tamil.utf8.splitMeiUyir(first_letter)
	if type(root_words)==tuple:
	    root_first=root_words[0]
	else:
	    root_first=root_words
	if root_first in உயிர்_முதலெழுத்து:
	    return True
	else:
	    return False

for word in sentence.split():
	print(word, uyir_check(word, உயிர்_முதலெழுத்து))
# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
