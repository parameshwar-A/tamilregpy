
from meymayakkamfinal import *
from word_ending import *

word=input("Enter the word you want to check: ")
ruleset={
    "meymayakkam":(meymayakkam1,meymayakkam2,meymayakkam3,meymayakkam4,meymayakkam5,meymayakkam6,meymayakkam7,meymayakkam8),
    "wordending": (uyir_check, mellinam_check, idaiyinam_check, oorezhuthoorumozhi_check, alapedai_check, suttu_check, vinaa_check)
}
meymayakkam_checks=[]
for check in ruleset["meymayakkam"]:
    output=check(word)
    if output==None:
        continue
    else:
        meymayakkam_checks.append(output)
        
wordending_checks=[]
for check in ruleset["wordending"]:
    output=check(word)
    if output==None:
        continue
    else:
        wordending_checks.append(output)

print(f"Meymayakkam check for {word}:", any(meymayakkam_checks))
print(f"wordending check for {word}:", any(wordending_checks))
