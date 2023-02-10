#tholkaappiyar_Word_Ending_Rule_1_opentamil.py
import tamil
#To use this package and run this script kindly install open-tamil package using
# Open terminal > type "pip install open-tamil" > Then wait for installations
# Once done you can use import tamil 
# இதன் இறுதியில் குறிப்பு தந்துள்ளேன் கவனிக்கவும்.
sentence = "அவன் ஒரு மொழியைத் தாய்மொழியாகக் கொண்டு பேசும் வெரிந் பாரிந் மக்களின் எண்ணிக்கை அடிப்படையில் உரிஞ் கரிஞ் பதினெட்டாவது இடத்தில் உள்ளது"
mellinam_list=["ஞ்", "ண்", "ந்", "ம்", "ன்"]
def uyir_check(word, mellinam_list):
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

for word in sentence.split():
	print(word, uyir_check(word,mellinam_list))
	
# இதனை இயக்கும் பொழுது சிக்கல் உள்ளது. கூடுதல் விதியை 'ஞ்', 'ந்' ஆகிய எழுத்துக்களுக்கு உருவாக்க வேண்டும்.
#அவன் True
#ஒரு False
#மொழியைத் False
#தாய்மொழியாகக் False
#கொண்டு False
#பேசும் True
#வெரிந் True
#பாரிந் True > False # ‘ந்’ என்பது பொருந் (ஒத்திருத்தல்), வெரிந் (முதுகு) என்னும் இருசொற்களில் மட்டும் இறுதியில் வந்தது
#மக்களின் True
#எண்ணிக்கை False
#அடிப்படையில் False
#உரிஞ் True
#கரிஞ் True > False # ஞ்’ என்பது உரிஞ் (தேய்த்தல்) என்னும் ஒரு சொல்லில் மட்டும் இறுதியில் வந்தது.
#பதினெட்டாவது False
#இடத்தில் False
#உள்ளது False
