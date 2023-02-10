#tholkaappiyar_Word_Ending_Rule_1_opentamil.py
import tamil
# To use this package and run this script kindly install open-tamil package using
# Open terminal > type "pip install open-tamil" > Then wait for installations
# Once done you can use import tamil 

sentence = "அவன் ஒரூஉ அங்கு இவ்வாறு பேசும் ஆ ஈ ஊ ஏ ஐ ஓ இவ்விடத்தில் உள்ளது"
oorezhuthoorumozhi_list=["ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ"]
def uyir_check(word, oorezhuthoorumozhi_list):
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

for word in sentence.split():
	print(word, uyir_check(word, oorezhuthoorumozhi_list))
	
# சான்று
#அவன் False
#ஒரூஉ False
#அங்கு False
#இவ்வாறு False
#பேசும் False
#ஆ True
#ஈ True
#ஊ True
#ஏ True
#ஐ True
#ஓ True
#இவ்விடத்தில் False
#உள்ளது False
#
