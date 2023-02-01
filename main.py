
from meymayakkamfinal import *

word=input("Enter the word you want to check: ")
ruleset={
    "meymayakkam":(meymayakkam1,meymayakkam2,meymayakkam3,meymayakkam4,meymayakkam5,meymayakkam6,meymayakkam7)
}
meymayakkam_checks=[]
for check in ruleset["meymayakkam"]:
    output=check(word)
    if output==None:
        continue
    else:
        meymayakkam_checks.append(output)

print(f"Meymayakkam check for {word}:", any(meymayakkam_checks))
