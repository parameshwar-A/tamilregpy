# தொல்காப்பியர்_மொழியிறுதி_விதிகள் (Tholkaappiar_word_ending_rule)
# இந்நிரலாக்கம் தமிழ் மொழித் தரவுகளைத் தொல்காப்பிய விதிகளைக் கொண்டு கணினி வழியாக மொழியிறுதி எழுத்துக்களைக் கண்டறிவதற்கான நிரல் தொகுப்பாகும்.
# இந்நிரலாக்கத்தை உருவாக்கியவர்கள் - அ.பரமேசுவரன், முனைவர் த. சத்தியராஜ் (நேயக்கோ)
import tamil
# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.

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

def alapedai_check(word):
    alapedai_list=["அ", "இ", "உ", "எ", "ஒ"]
    last_letter=tamil.utf8.get_letters(word)[-1]
    if last_letter in alapedai_list:

        return True
    else:
        return False

# இது அளபெடை எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.


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


def vinaa_check(word):
    vallinam_list=["க்", "ச்", "த்", "ப்", "வ்", "ங்", "ந்"]
    if len(word)<2:
	    return False
    first_letter=tamil.utf8.get_letters(word)[0]
    second_letter=tamil.utf8.get_letters(word)[1]

    if first_letter == "எ" and second_letter in vallinam_list:
        return True
    else:
        return False

# இது வினா எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

# இது இறுதியாக அனைத்து விதிகளையும் பொருத்திப் பார்த்து பதில் அளிப்பதற்குரிய நிரலாகும்.
