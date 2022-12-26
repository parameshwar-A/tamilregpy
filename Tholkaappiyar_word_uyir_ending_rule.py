#tholkaappiyar_Word_Ending_Rule_1_opentamil.py
import tamil
#To use this package and run this script kindly install open-tamil package using
# Open terminal > type "pip install open-tamil" > Then wait for installations
# Once done you can use import tamil 
sentence = "ஒரு மொழியைத் தாய்மொழியாகக் கொண்டு பேசும் மக்களின் எண்ணிக்கை அடிப்படையில் பதினெட்டாவது இடத்தில் உள்ளது"
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

for word in sentence.split():
	print(word, uyir_check(word,uyir_list))
	
