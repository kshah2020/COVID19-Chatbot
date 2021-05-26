import csv

def PAVaccines(zip2): 
    sites = []
    finalSites = "Your nearest vaccination site(s) are: "
    with open('PAData.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            zipCode = row["ZIP Code"]
            if(int(zipCode) == int(zip2)):
                sites.append(row["Clinic Name"].capitalize() + ": " + row["Street Address"] + " " + row["City"] + ", PA " + row["ZIP Code"])
        #print(sites)
    num = 0 
    sites2 = ["N/A","N/A","N/A"] 
    while num < 3: 
        if(num > len(sites)-1): 
            break
        sites2[num] = sites[num]
        num+=1
    return sites2
