import matplotlib.pyplot as plt
import numpy as np
import datetime
import requests
#import pandas as pd
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from matplotlib import pyplot as plt
from matplotlib import style

#df = pd.read_csv('Downloads/death_vs_beds.csv')
matplotlib.use('agg')
matplotlib.pyplot.switch_backend('Agg')
def createGraph(zipcode):
    x = datetime.datetime.now()
    m = x.strftime("%m")
    d = int(x.strftime("%d"))-1
    #d = "16"
    y = x.strftime("%Y")
    currentDate = "total"+str(m)+"_"+str(d)+"_"+str(y)

    dates =[]
    dateinfo = []
    cases = [] 

    for num in range(1,8): 
        today = datetime.date.today()
        days_ago = str(today - datetime.timedelta(days=(8-num)))
        days = days_ago.split("-")
        dates.append(days[1] + "/" + days[2])
        dateinfo.append("total"+str(days[1])+"_"+str(days[2])+"_"+str(days[0]))

    url = "https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MDCOVID19_MASTER_ZIP_CODE_CASES/FeatureServer/0/query?where=ZIP_CODE%20%3D%20"


    url += "'"+ str(zipcode)+"'""&outFields=*&outSR=4326&f=json"

    r = requests.get(url = url)

    data = r.json()

    listData = data["features"]
    dictionaryData = listData[0]
    for eachDate in dateinfo: 
        cases.append(dictionaryData["attributes"][eachDate])



    x = dates
    y = cases

    plt.xticks(rotation=45)
    plt.yticks(np.arange(min(cases), max(cases)+1, 5.0))
    plt.yticks(rotation=0)
    # Show the major grid lines with dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-')

    #plt.minorticks_on()
    #plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    graphCases = plt.figure()
    #graphCases.title("7 Day Cases in " + str(zipcode) + "\n(Note Graph Does Not Start At Zero)")
    #graphCases.xlabel('Date')
    #graphCases.ylabel('Covid Cases')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title('7 Day Cases in ' + str(zipcode) + "\n(Note Graph Does Not Start At Zero)")
    axis.set_xlabel('Date')
    axis.set_ylabel('Covid Cases')
    #axis.set_rotation(45)
    axis.plot(x, y)
    #graphCases.plot(x,y)
    #graphCases.scatter(x,y)
    #graphCases.savefig("static/cases_data"+str(zip)+".png")
    #graphCases.close()
    return fig
    #plt.show() 

    
 