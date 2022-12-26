#tholkaappiyar_Word_Ending_Rule_1_opentamil.py
import tamil
# To use this package and run this script kindly install open-tamil package using
# Open terminal > type "pip install open-tamil" > Then wait for installations
# Once done you can use import tamil 
# இதன் இறுதியில் குறிப்பு தந்துள்ளேன் கவனிக்கவும்.
sentence = "அவன் ஒரு அவ் இவ் உவ் தெவ் பேசும் வெரிந் பாரிந் மக்களின் தமிழ் தரிவ் அவர் பாரிவ் பார்த்தார் வாரிவ் அவ்கருத்து அவள் உரிஞ் கேட்டாள் கரிஞ் பதினெட்டாவது இடத்தில் உள்ளது"
idaiyinam_list=["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"]
def uyir_check(word, idaiyinam_list):
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

for word in sentence.split():
	print(word, uyir_check(word, idaiyinam_list))
	
# இதனை இயக்கும் பொழுது சிக்கல் உள்ளது. கூடுதல் விதியை 'ஞ்', 'ந்' ஆகிய எழுத்துக்களுக்கு உருவாக்க வேண்டும்.
#அவ் True
#இவ் True
#உவ் True
#தெவ் True
#பேசும் False
#வெரிந் False
#பாரிந் False
#மக்களின் False
#தமிழ் True
#தரிவ் True > False # ‘வ்’ என்பது அவ், இவ், உவ், தெவ் (பகை) என்னும் நான்கு சொற்களில் மட்டுமே இறுதியில் வந்தது.
#அவர் True
#பாரிவ் True > False
#பார்த்தார் True
#வாரிவ் True > False
#அவ்கருத்து False
#அவள் True
#உரிஞ் False
#கேட்டாள் True
#கரிஞ் False
#பதினெட்டாவது False
#இடத்தில் True
#உள்ளது False
