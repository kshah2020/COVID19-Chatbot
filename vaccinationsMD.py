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

#https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=1%3D1&outFields=*&outSR=4326&f=json
def vaccineMD(zipcode): 
    url = "https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    r = requests.get(url = url)

    data = r.json()
    listData = data["features"]

    sites = [] 
    #zipcode = 21044

    for eachSite in listData: 
        siteData = eachSite["attributes"]
        address = siteData['fulladdr']

        split = address.split("MD ")
        if(len(split) == 1): 
            split = address.split("Maryland ")
            if(len(split)==1): 
                split=["",""]
        zipcode2 = split[1] 

        if(zipcode2 == str(zipcode)): 
            sites.append(siteData["name"].capitalize()  + ": " + address)

    finalSites = "Your nearest vaccination site(s) are: "
    num = 0 
    sites2 = ["Not Available","Not Available","Not Available"] 
    while num < 3: 
        if(num > len(sites)-1): 
            break
        sites2[num] = sites[num]
        num+=1
    return sites2



