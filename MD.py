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

#MD 
def showChange(dateC, dateP):
   change = dateC-dateP
   if(change < 0):
       return "Since yesterday, there has been a drop in cases by " + "{:,}".format(int(abs(change))) + " cases"
   elif(change > 0):
       return "Since yesterday, there has been a increase in cases by " + "{:,}".format(int(change)) +  " cases"
 
def testingMD(zipcode):
    url = "https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MDCOVID19_MASTER_ZIP_CODE_CASES/FeatureServer/0/query?where=ZIP_CODE%20%3D%20"


    url += "'"+ str(zipcode)+"'""&outFields=*&outSR=4326&f=json"

    r = requests.get(url = url)

    data = r.json()

    listData = data["features"]
    dictionaryData = listData[0]
 
    x = datetime.datetime.now()
    m = x.strftime("%m")
    d = int(x.strftime("%d"))-1
    #d = "16"
    y = x.strftime("%Y")
    currentDate = "total"+str(m)+"_"+str(d)+"_"+str(y)
    currentDate2 = str(m)+"_"+str(d)+"_"+str(y)
 
   #return "Total Cases in " + zipcode + ": " + str(dictionaryData["attributes"][currentDate]))
 
    y = datetime.datetime.now()
    m = y.strftime("%m")
    d = int(y.strftime("%d")) - 2
    #d = "15"
    y = y.strftime("%Y")
    previousDate = "total"+str(m)+"_"+str(d)+"_"+str(y)
 
    if previousDate in dictionaryData["attributes"].keys():
        string2 = showChange(dictionaryData["attributes"][currentDate], dictionaryData["attributes"][previousDate])

    return "Total Cases in " + zipcode + " as of " + currentDate2 + ": " + "{:,}".format(int(dictionaryData["attributes"][currentDate])), string2

def totalMD():
  URL = "https://data.cdc.gov/resource/9mfq-cb36.json?state=MD&submission_date="
  
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
       return "Total Cases in Maryland as of " + str(currentDate2) +": " + "{:,}".format(int(data2["tot_cases"]))
 
