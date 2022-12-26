#tholkaappiyar_Word_Ending_Rule_1_opentamil.py
import tamil
# To use this package and run this script kindly install open-tamil package using
# Open terminal > type "pip install open-tamil" > Then wait for installations
# Once done you can use import tamil 
# இதன் இறுதியில் குறிப்பு தந்துள்ளேன் கவனிக்கவும்.
# முதல் எழுத்தை வைத்து விதி எழுதவேண்டும்.

sentence = "அவன் எப்படி எங்கு எவ்வாறு எந்த அங்கு இவ்வாறு பேசும் ஆ ஈ ஊ ஏ ஐ ஓ இவ்விடத்தில் உள்ளது"
vinaavezhuthu_list=["எ"]
def uyir_check(word, vinaavezhuthu_list):
	last_letter=tamil.utf8.get_letters(word)[-1]
	root_words=tamil.utf8.splitMeiUyir(last_letter)
	if type(root_words)==tuple:
	    root_last=root_words[-1]
	else:
	    root_last=root_words
	if root_last in vinaavezhuthu_list:
	    return True
	else:
	    return False

for word in sentence.split():
	print(word, uyir_check(word, vinaavezhuthu_list))
	
# இதனை இயக்கும் பொழுது சிக்கல் உள்ளது.
#அவன் False
#எப்படி False > True
#எங்கு False > True
#எவ்வாறு False > True
#எந்த False > True
#அங்கு False
#இவ்வாறு False
#பேசும் False
#ஆ False
#ஈ False
#ஊ False
#ஏ False
#ஐ False
#ஓ False
#இவ்விடத்தில் False
#உள்ளது False
