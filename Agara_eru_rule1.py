# நிலைமொழியில் அகர ஈற்றுச் சொற்கள் நிற்க (விள), 
# வருமொழி முதலில் க, ச, த, ப எழுத்துக்களில் தொடங்கும் சொற்கள் (+ குறிது, + சிறிது, + பெரிது) வரும் பொழுது
# வல்லினம் மிகும் (க், ச், த், ப்) 
# விள + குறிது = விளக்குறிது
#1. செய்யிய என்னும் வாய்பாட்டு வினையெச்சங்களின் முன்னர் வரும் வல்லினம் (க, ச, த, ப) இயல்பாகும்.

#சான்று:

#காணிய + சென்றான்  
# காணிய சென்றான் (காண்பதற்குச் சென்றான்)
#உண்ணிய + போனான்
#= உண்ணிய போனான் (உண்பதற்குப் போனான்)

import tamil

def agara_eru(first_word, second_word):
    last_letter_first_word = tamil.utf8.get_letters(first_word)[-1]
    root_words=tamil.utf8.splitMeiUyir(last_letter_first_word)
    if type(root_words)==tuple and root_words[-1]=="அ":
        first_letter_second_word = tamil.utf8.get_letters(second_word)[0]
        root_word_second = tamil.utf8.splitMeiUyir(first_letter_second_word)
        if type(root_word_second)==tuple and (root_word_second[0] in ("க்", "ச்", "த்", "ப்")):
            return first_word+root_word_second[0]+second_word
        else:   
            return None
    else:
        return None
        
print(agara_eru(input("Enter first word: "),input("Enter Second word: ")))

#Tested words
# விள + குறிது = விளக்குறிது
# காண + சென்றான் = காணச்சென்றான்  
#  விட + சொல் = விடச்சொல்

# The words which does not satisfy agara eru conditions will be returned None
