from gui import chatbot
from flask import Flask, render_template, request
from newspaper import Article
import random 
import string
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import warnings 
import requests
import datetime
warnings.filterwarnings("ignore")
from pprint import pprint
import zipcodes

from MD import testingMD, totalMD
from VA import testingVA, totalVA
from graph import createGraph
from PA import testingPA, totalPA
from vaccinationsMD import vaccineMD
from csvreader import PAVaccines


def justZipcode(zipCode): 
    zipcodeInfo = zipcodes.matching(str(zipCode))
    if zipcodeInfo != []: 
        zipcodeInfo = zipcodes.matching(str(zipCode))[0]
    if(zipcodeInfo):
        state = zipcodeInfo["state"]
    if state=="MD": 
            return str(vaccineMD(zipCode)) + " " + str(testingMD(zipCode))
    if state =="VA":
        return testingVA(zipCode)
    if state=="PA": 
        county = zipcodeInfo["county"]
        county = county.split(" ")[0].lower() 
        return str(PAVaccines(zipCode)) + " " + str(testingPA(county)) 

def findTask(prompt): 
    prompt2 = ""
    tokenized_word=word_tokenize(prompt)

    if "help" in tokenized_word or "menu" in tokenized_word or "options" in tokenized_word or "home" in tokenized_word: 
        return "help"

    if len(prompt)==5 and prompt.isdigit() and len(tokenized_word)==1: 
        zipCode = prompt
        return justZipcode(zipCode)

    matchingWords = []
    
    paCounties = ["adams", "allegheny", "armstrong", "beaver", "bedford", "berks", "blair", "bradford", "bucks", "butler", "cambria", "cameron", "carbon", "centre", "chester", "clarion", "clearfield", "clinton", "columbia", "crawford", "cumberland", "dauphin", "delaware", "elk", "erie", "layette", "forest", "franklin", "fulton", "greene", "huntingdon", "indiana", "jefferson", "juniata", "lackawanna", "lancaster", "lawrence", "lebanon", "lehigh", "luzerne", "lycoming","york","wyoming","westmoreland","wayne","washington","warren","venago","union","tioga","susquehanna","sullivan","somerset","snyder","schuylkill","potter","pike","philadelphia","perry","northumberland","northampton","montour","montgomery","moroe","mifflin","mercer","mckean"]


    zipCode = 0 
    county = ""
    state = ""

    for eachWord in tokenized_word: 
        #if eachWord=="cases" or eachWord == "change" or eachWord == "total": 
        #matchingWords.append(eachWord)
        if len(eachWord)==5 and eachWord.isdigit(): 
            zipCode = eachWord 
        if eachWord in paCounties and eachWord.isalpha(): 
            county = eachWord

    if ("cases" in tokenized_word or "total" in tokenized_word) and ( "md" in tokenized_word or "maryland" in tokenized_word):
        return totalMD()

    elif ("vaccine" in tokenized_word or "vaccines" in tokenized_word or "vaccinations" in tokenized_word) or ( "sites" in tokenized_word or "locations" in tokenized_word):    
        print(zipCode)
        if zipCode != 0: 
            prompt2 = "vaccine"
            zipcodeInfo = zipcodes.matching(str(zipCode))[0]
            if(zipcodeInfo):
                state = zipcodeInfo["state"]
            if(state == "MD"):
                return vaccineMD(zipCode)
            elif(state == "PA"): 
                return PAVaccines(zipCode)
            else:
                return "No data available for this state"
        else: 
            return "No"
    elif "vaccine" in tokenized_word or "vaccines" in tokenized_word or "vaccinations" in tokenized_word or "vaccination" in tokenized_word: 
        if zipCode == 0: 
            return "No"
    elif ("cases" in tokenized_word or "total" in tokenized_word) and ( "va" in tokenized_word or "virginia" in tokenized_word):
        return totalVA()

    elif ("cases" in tokenized_word or "total" in tokenized_word) and ( "pa" in tokenized_word or "pennsylvania" in tokenized_word):
        return totalPA()

    elif "graph" in tokenized_word: 
        return zipCode
    elif "cases" in tokenized_word or "total" in tokenized_word or "change" in tokenized_word or "outbreak" in tokenized_word or "outbreaks" in tokenized_word: 
        if county != "": 
            return testingPA(county)
        else:
            zipcodeInfo = zipcodes.matching(str(zipCode))
            if zipcodeInfo != []: 
                zipcodeInfo = zipcodes.matching(str(zipCode))[0]
            if(zipcodeInfo):
                state = zipcodeInfo["state"]
            if(state=="PA"):
                county = zipcodeInfo["county"]
                county = county.split(" ")[0].lower()
            if(state=="MD" and zipCode != 0):
                prompt2 = "cases"
                return testingMD(zipCode) 
            #elif(state=="MD"and zipCode==0): 
                #return "None MD"
            elif(state=="VA" and zipCode != 0):
                return testingVA(zipCode) 
            #elif(state=="VA"and zipCode==0): 
             #   print("What is your zip code?")
              #  zipCode = input() 
               # testingVA(zipCode)
            elif(state=="PA" and county != ""):
                return testingPA(county) 
            #elif(state=="PA"and county==""): 
             #   print("What is your county?")
              #  county = input().lower()  
               # tokenized_county=word_tokenize(county)
                #for eachWord in tokenized_word: 
                #if eachWord in paCounties and eachWord.isalpha(): 
                 #   county = eachWord
                #testingPA(county)

            elif(state==""and zipCode==0): 
                return "No"
    
    else: 
        return "This capability isn't working right now! Try being more specific!"
       #         zipcodeInfo = zipcodes.matching(str(zipCode))
        #        if zipcodeInfo != []: 
         #           zipcodeInfo = zipcodes.matching(str(zipCode))[0]
          #      if(zipcodeInfo):
           #         state = zipcodeInfo["state"]
            #    if state=="MD": 
             #       testingMD(zipCode) 
              #  if state =="VA":
               #     testingVA(zipCode)
               # if state=="PA": 
                #    county = zipcodeInfo["county"]
                 #   county = county.split(" ")[0].lower() 
                  #  testingPA(county)