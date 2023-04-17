
from meymayakkamfinal import *
from word_ending import *
from word_starting import *
import csv

#word=input("Enter the word you want to check: ")
ruleset={
    "meymayakkam":(meymayakkam1,meymayakkam2,meymayakkam3,meymayakkam4,meymayakkam5,meymayakkam6,meymayakkam7,meymayakkam8),
    "wordending": (uyir_check, mellinam_check, idaiyinam_check, oorezhuthoorumozhi_check, alapedai_check, suttu_check, vinaa_check),
    "wordstarting" : (uyirezhuthu_check , uyirmei_ka_check , uyirmei_sa_check , uyirmei_nga_check  , uyirmei_ta_check , uyirmei_na_check , uyirmei_pa_check , uyirmei_ma_check , uyirmei_ya_check , uyirmei_va_check)
}
def do_meymayakkam_check(word):
    meymayakkam_checks=[]
    for check in ruleset["meymayakkam"]:
        output=check(word)
        if output==None:
            continue
        else:
            meymayakkam_checks.append(output)
    return meymayakkam_checks

def do_wordending_check(word):        
    wordending_checks=[]
    for check in ruleset["wordending"]:
        output=check(word)
        if output==None:
            continue
        else:
            wordending_checks.append(output)
    return wordending_checks

def do_wordstarting_check(word):
    wordstarting_checks=[]
    for check in ruleset["wordstarting"]:
        output=check(word)
        if output==None:
            continue
        else:
            wordstarting_checks.append(output)
    return wordstarting_checks


filename=input("Enter the name of the file: ")


with open(filename, "r+") as dataset:
    csvreader=csv.reader(dataset)
    header=next(csvreader)
    for row in csvreader:
        word=row[2]
        if len(word.split())>1 or len(word)<=2:
            #This is to skip multi word (அல்லும் பகலும்) and word with single letter (தீ)
            continue
        print(f"{word}: ")
        meymayakkam_checks=do_meymayakkam_check(word)
        wordending_checks=do_wordending_check(word)
        wordstarting_checks=do_wordstarting_check(word)
        print(f"\tMeymayakkam check for {word}:", any(meymayakkam_checks))
        print(f"\twordending check for {word}:", any(wordending_checks))
        print(f"\twordstarting check for {word}:", any(wordstarting_checks))




