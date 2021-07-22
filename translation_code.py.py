# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from englisttohindi.englisttohindi import EngtoHindi
from deep_translator import GoogleTranslator
import traceback

# Opening JSON file
f = open('sentences.json',)
  
# returns JSON object as 
# a dictionary







data = json.load(f)



list_en = []
list_hin =[]
k=0
   
try:
    with open("myfile_translated_hindi_5.txt", "wb") as f1:
        for i in data:
            k+=1
            if k<60496:
                continue;
            if k%100==0:
                print("here completed +",k);
            #print(i)
            res =  GoogleTranslator(source='auto', target='hi').translate(i)
            if k%10==0:
                print(res)
            f1.write(res.encode("utf-8"))
            f1.write(bytes('\n',"utf-8"))
            list_hin.append(res)
            
except:
    f1.close()
    print("in except error")
    traceback.print_exc()

f1.close()



