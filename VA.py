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

#VA
def testingVA(zipcode):
    URL = "https://data.virginia.gov/resource/8bkr-zfqv.json"

    r = requests.get(url = URL)
    data = r.json()

    x = datetime.datetime.now()
    m = x.strftime("%m")
    d = int(x.strftime("%d"))
    y = x.strftime("%Y")
    currentDate = str(y)+"-"+str(m)+"-"+str(d)
    currentDate2 = str(m)+"_"+str(d)+"_"+str(y)

    currentDate+="T00:00:00.000"

    x = datetime.datetime.now()
    m = x.strftime("%m")
    d = int(x.strftime("%d"))-1
    y = x.strftime("%Y")
    previousDate = str(y)+"-"+str(m)+"-"+str(d)

    previousDate+="T00:00:00.000"

    currentDateInfo = 0 
    previousDateInfo = 0 


    for eachData in data:
        x = eachData["zip_code"]
        if(x==zipcode):
            string1 = "Total Cases in " + str(zipcode) + " as of " + currentDate2 + ": "+ "{:,}".format(int(eachData["number_of_cases"])) + ".\n"
            break

    for eachData in data:
        x = eachData["report_date"]
        z = eachData["zip_code"]
        if(x==previousDate and z == zipcode):
            previousDateInfo = int(eachData["number_of_cases"])
        if(x==currentDate and z == zipcode):
            currentDateInfo = int(eachData["number_of_cases"])

    change = currentDateInfo - previousDateInfo

    if(change < 0):
        return string1,"Since yesterday, there has been a drop in cases by " + str(abs(change)) + " cases"
    elif(change > 0):
        return string1,"Since yesterday, there has been a increase in cases by " + str(change) +  " cases"
    else: 
        return string1 + " Since yesterday, there has been a increase in cases by " + str(0) +  " cases"


def totalVA():
  URL = "https://data.cdc.gov/resource/9mfq-cb36.json?state=VA&submission_date="
  
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
       return "Total Cases in Virginia as of " + currentDate2 + ": " + "{:,}".format(int(data2["tot_cases"]))
 