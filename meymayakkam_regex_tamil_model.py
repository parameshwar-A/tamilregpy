# Python project - Kanchilug
#regex modle in meymayakkam Tholkappaiyar theory
import re
# தமிழ் மொழியைப் பிழையில்லாமல் எழுதுவதற்கு மெய்மயக்கங்கள் குறித்த புரிதல் தேவைப்படுகிறது. 
# ஏனெனில் மயக்கங்களைப் புரிந்துகொள்ளும்பொழுது பிழைகள் தவிர்க்கப்படுகின்றன. 
# எ-டு. மார்ரி – மாரி, கார்ரி – காரி, அண்னன் – அண்ணன், அண்னி - அண்ணி

# புதிதாகத் தமிழ் மொழியை எழுத நினைப்போர் இந்த எடுத்துக்காட்டில் அமைந்துள்ளமை போன்று எழுத முற்படுவதைப் பார்க்கலாம். 
# இதனைச் சரிசெய்ய மெய்மயக்கங்களை அறிய வேண்டும் என வலியுறுத்தப்படுகிறது. 

# எழுத்துக்களின் மயக்கம் - எழுத்துக்கள் மயங்கும் முறையைத் தொல்காப்பியர் இரண்டு வகையாகப் பிரிப்பார். 
## ஒன்று: உடனிலை மெய்மயக்கம்.
### உடனிலை மெய்மயக்கம் என்று கூறப்படுவது தன் எழுத்து தன்னோடு மயங்கி வருவது. எ-டு. பாக்கு, தேக்கு, நோக்கு.
### இதில் 'க்க்' எழுத்துக்கள் தொடர்ந்து வருவதை பார்க்கலாம். இதனைத்தான் உடனிலை மெய்ம்மயக்கம் என்கிறோம்.

## இரண்டு: வேற்றுநிலை மெய்ம்மயக்கம்
### வேற்றுநிலை மெய்மயக்கம்  எனப்படுவது வேறு வேறு எழுத்துக்கள் மயங்குவது. எ-டு. வாங்கு, பஞ்சு, கொண்டு, வந்து, பம்பரம், சென்றான்.
### இவற்றில் 'ங்கு', 'ஞ்சு', 'ண்டு', 'ந்து', 'ம்ப', 'ன்ற' ஆகிய எழுத்துக்கள் மயங்கி வருவதைப் பார்க்கலாம். 
### இதனையே நாம் வேற்றுநிலை மெய்ம்மயக்கம் என்கிறோம்.
### தமிழ் மொழியில் உள்ள பிழையைத் தவிர்க்க, தொல்காப்பியம் எழுத்ததிகாரம் நூன்மரபில் சில விதிகள் தரப்பெற்றுள்ளன. அவை;

## 1) ட் ற் ல் ள் + க ச ப
# ஒரு சொல்லில் ட், ற், ல், ள் ஆகிய எழுத்துக்களுக்குப் பின்பு ஆகிய க, ச, ப ஆகிய எழுத்துக்கள் மயங்கி வரும். எ-டு. கேட்க, கற்க, செல்க, கொள்க.

x=int(input("சொல்லை உள்ளீடு செய்: "))

# Commented by paramesh
#meymayakkam_regex_tamil_model.py", line 25, in <module>
#    x=int(input("சொல்லை உள்ளீடு செய்: "))
#    ValueError: invalid literal for int() with base 10:
#

# The error is arising at line 25, when you look at it you converted the text to integer, which will not happen. So remove int typecasting in line 25.


txt = ["ட் ற் ல் ள் + க ச ப"]

if re.match('.*ட்க ', '.*ற்க ', '.*ல்க ', '.*ள்க ', '.*ட்ச ', '.*ற்ச ', '.*ல்ச ', '.*ள்ச ', '.*ட்ப ', '.*ற்ப ', '.*ல்ப ', '.*ள்ப ', text):
	print("இது சரியான சொல்லாகும்.")
else:
	print("இது பிழையான சொல்லாகும்.")
	
## 2) ல் ள் + ய வ
# ல், ள் ஆகிய எழுத்துக்களுக்குப் பின்பு ய, வ எழுத்துக்கள் மயங்கி வரும். எ-டு. கொல்யானை, வெள்வளை.


## 3) ங் ஞ் ண் ந் ம் ன் + தத்தமிசைகள் (க ச ட த ப ற)
# மெல்லின எழுத்துக்கள் ஆகிய ங், ஞ், ண், ந், ம், ன் ஆகிய எழுத்துக்களுக்குப் பின்பு அதனுடைய ஒத்த ஒலிகளாக அறியப்படுகின்ற வல்லின எழுத்துக்கள் ஆகிய க, ச, ட, த, ப, ற ஆகிய எழுத்துகள் மயங்கி வரும். 
# இதனை அடிப்படையாக வைத்தே க்ங், ச்ஞ், ட்ண், த்ந், ப்ம், ற்ன் என்ற மெய் எழுத்து வரிசைமுறை தமிழ்மொழியில் இடம்பெறுகின்றன. 
# இதனை இப்படிப் புரிந்துகொள்ளலாம். ங் என்ற எழுத்தை அடுத்து க எழுத்து வரும். 
# அதுபோல் ஞ்ச, ண்ட, ந்த, ம்ப, ன்ற என்ற என்ற எழுத்துக்கள் மயங்கி வருவதை நாம் பார்க்கமுடியும். 
# எ-டு. மாங்காய், பிஞ்சு, மண்டை, வந்து, வம்பு, சென்ற.


## 4) ஞ் ந் ம் வ் + ய
# ஞ். ந், ம், வ் எழுத்துக்களுக்குப் பின்பு ய எழுத்து மயங்கி வரும். எ-டு. உரிஞ்யாது, தெவ்யாது.

## 5) ம் + வ
# ம் எழுத்துக்களுக்குப் பின்பு ய எழுத்து மயங்கி வருவதைப்போல் வ எழுத்தும் மயங்கி வரும். எ-டு. நிலம்வலிது.

## 6) ய் ர் ழ் + க ச த ப ஞ ந ம ய வ ங
# ய், ர், ழ் ஆகிய எழுத்துக்களுக்குப் பின்பு க, ச, த, ப, ஞ, ந, ம, ய, வ, ங எழுத்துக்கள் மயங்கி வரும். எ-டு. நாய்க்கடி, வாழ்க்கை, வேர்வை, வாழ்வு, வேய்ங்குழல்


## 7) ர ழ அலங்கடை
# ர, ழ என்ற எழுத்துக்கள் தவிர பிற எழுத்துக்கள் தன் எழுத்துக்களோடு தன் எழுத்துக்கள் மயங்கி வரும். 
# எ-டு. வாக்கு, இங்ஙனம், செஞ்ஞாயிறு, பச்சை, அட்டை, அண்ணன், அண்ணி





