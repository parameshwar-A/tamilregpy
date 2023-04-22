
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

report={
'total_words':0,
'skipped_words':0,
'meymayakkam_correct':0,
'wordending_correct':0,
'wordstarting_correct':0
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
column_num=int(input("Enter the column number which has word to check: "))


with open(filename, "r+") as dataset:
    csvreader=csv.reader(dataset)
    header=next(csvreader)
    for row in csvreader:
        word=row[column_num-1]
        report['total_words']=report.get('total_words')+1
        if len(word.split())>1 or len(word)<=2:
            #This is to skip multi word (அல்லும் பகலும்) and word with single letter (தீ)
            report['skipped_words']=report.get('skipped_words')+1
            continue
        print(f"{word}: ")
        meymayakkam_checks=do_meymayakkam_check(word)
        wordending_checks=do_wordending_check(word)
        wordstarting_checks=do_wordstarting_check(word)
        print(f"\tMeymayakkam check for {word}:", any(meymayakkam_checks))
        if any(meymayakkam_checks):
            report['meymayakkam_correct']=report.get('meymayakkam_correct')+1
        print(f"\twordending check for {word}:", any(wordending_checks))
        if any(wordending_checks):
            report['wordending_correct']=report.get('wordending_correct')+1
        print(f"\twordstarting check for {word}:", any(wordstarting_checks))
        if any(wordstarting_checks):
            report['wordstarting_correct']=report.get('wordstarting_correct')+1



print(f"Report of {filename}")
print(f"மொத்த சொற்களின் எண்ணிக்கை : {report['total_words']}")
print(f"சரி பார்க்காத ஓர் எழுத்து சொற்கள் மற்றும் இரு சொற்களின் எண்ணிக்கை  : {report['skipped_words']}")
print(f"மெய்ம்மயக்க விதிப்படி சரியான சொற்களின் எண்ணிக்கை  : {report['meymayakkam_correct']}")
print(f"மொழி முதல் எழுத்து  விதிப்படி சரியான சொற்களின் எண்ணிக்கை  : {report['wordstarting_correct']}")
print(f"மொழி  இறுதி எழுத்து  விதிப்படி சரியான சொற்களின் எண்ணிக்கை  : {report['wordending_correct']}")
