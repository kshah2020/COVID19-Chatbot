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
#PA
def testingPA(county):
    URL = "https://data.pa.gov/resource/j72v-r42c.json?county="

    countytemp = county[0].upper() 
    county = countytemp + county[1:len(county)]

    #print("What is your county")
    #couties = ["Allegheny","Adams", "Armstrong", "Beaver", "Bedford", "Berks", "Blair", "Bradford", "Bucks", "Butler", "Cambria", "Cameron", "Carbon", "Centre", "Chester", "Clarion", "Clearfield", "Clinton", "Columbia","Crawford"]
    #county = input()
    URL += county
    URL+="&date="

    x = datetime.datetime.now()
    m = x.strftime("%m")
    d = int(x.strftime("%d"))-2
    y = x.strftime("%Y")
    currentDate = str(y)+"-"+str(m)+"-"+str(d)
    currentDate2 = str(m)+"_"+str(d)+"_"+str(y)

    URL += currentDate+"T00:00:00.000"

    r = requests.get(url = URL)


    data = r.json()

    data2 = data[0]

    if(data2["cases_cume"]):
        string1 = "Total Cases in " + county + " County as of " + currentDate2 + ": " + "{:,}".format(int(data2["cases_cume"]))+ ".\n"

 
    change = int(data2["cases"])
    if(change < 0):
        return string1, "Since yesterday, there has been a drop in cases by " + str(abs(change)) + " cases"
    elif(change > 0):
        return string1, "Since yesterday, there has been a increase in cases by " + str(change) +  " cases"
    else: 
        return string1, "Since yesterday, there has been a increase in cases by " + str(0) +  " cases"

def totalPA():
  URL = "https://data.cdc.gov/resource/9mfq-cb36.json?state=PA&submission_date="
  
  x = datetime.datetime.now()
  m = x.strftime("%m")
  d = int(x.strftime("%d"))-2
  y = x.strftime("%Y")
  currentDate = str(y)+"-"+str(m)+"-"+str(d)
  currentDate2 = str(m)+"_"+str(d)+"_"+str(y)

  URL += currentDate+"T00:00:00.000"

  r = requests.get(url = URL)
  data = r.json()
  data2 = data[0]

  if(data2["submission_date"]):
       return "Total Cases in Pennsylvania as of " + currentDate2 + ": " + "{:,}".format(int(data2["tot_cases"]))
 