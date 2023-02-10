#tholkaappiyar_Word_Ending_Rule_1_opentamil.py
import tamil
# To use this package and run this script kindly install open-tamil package using
# Open terminal > type "pip install open-tamil" > Then wait for installations
# Once done you can use import tamil 
# இதன் இறுதியில் குறிப்பு தந்துள்ளேன் கவனிக்கவும்.
# முதல் எழுத்தை வைத்து விதி எழுதவேண்டும்.
sentence = "அவன் ஒரு அங்கு இவ்வாறு பேசும் அவர் பாரிவ் பார்த்தார் வாரிவ் அவ்கருத்து அவள் உரிஞ் இவ்விடத்தில் உள்ளது"
suttu_list=["அ", "இ", "உ"]
def uyir_check(word, suttu_list):
	last_letter=tamil.utf8.get_letters(word)[-1]
	root_words=tamil.utf8.splitMeiUyir(last_letter)
	if type(root_words)==tuple:
	    root_last=root_words[-1]
	else:
	    root_last=root_words
	if root_last in suttu_list:
	    return True
	else:
	    return False

for word in sentence.split():
	print(word, uyir_check(word, suttu_list))
	
# இதனை இயக்கும் பொழுது சிக்கல் உள்ளது.
#அவன் False > True
#ஒரு True > False
#அங்கு True # ஆனால் இறுதி எழுத்தைக் கணக்கிடுகின்றது.
#இவ்வாறு True # ஆனால் இறுதி எழுத்தைக் கணக்கிடுகின்றது.
#பேசும் False
#அவர் False
#பாரிவ் False
#பார்த்தார் False
#வாரிவ் False
#அவ்கருத்து True # ஆனால் இறுதி எழுத்தைக் கணக்கிடுகின்றது.
#அவள் False
#உரிஞ் False
#இவ்விடத்தில் False > True
#உள்ளது True > False # இது பயனிலை. 

