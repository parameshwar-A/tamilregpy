#tholkaappiyar_Word_Ending_Rule_1_opentamil.py
import tamil
# To use this package and run this script kindly install open-tamil package using
# Open terminal > type "pip install open-tamil" > Then wait for installations
# Once done you can use import tamil 
# இதன் இறுதியில் குறிப்பு தந்துள்ளேன் கவனிக்கவும்.

sentence = "அவன் ஒரூஉ அங்கு இவ்வாறு பேசும் அவராஅ பாரிவ் பார்த்தாரேஎ வாரிவ் கொடுப்பதூஉ அவள் உரிஞோஒ இவ்விடத்தில் உள்ளது"
alapedai_list=["அ", "இ", "உ", "எ", "ஒ"]
def uyir_check(word, alapedai_list):
	last_letter=tamil.utf8.get_letters(word)[-1]
	root_words=tamil.utf8.splitMeiUyir(last_letter)
	if type(root_words)==tuple:
	    root_last=root_words[-1]
	else:
	    root_last=root_words
	if root_last in alapedai_list:
	    return True
	else:
	    return False

for word in sentence.split():
	print(word, uyir_check(word, alapedai_list))
	
# இதனை இயக்கும் பொழுது சிக்கல் உள்ளது. 
# இறுதியில் இரண்டு உயிர் எழுத்துக்கள் வருவதற்கு ஏற்ப விதி எழுத வேண்டும்.
# அது நெடிலை அடுத்து வரும் உயிர் எழுத்தையே அளபெடை என்கின்றோம்.

#அவன் False
#ஒரூஉ True
#அங்கு True > False
#இவ்வாறு True > False
#பேசும் False
#அவராஅ True
#பாரிவ் False
#பார்த்தாரேஎ True
#வாரிவ் False
#கொடுப்பதூஉ True
#அவள் False
#உரிஞோஒ True
#இவ்விடத்தில் False
#உள்ளது True > False
#

