import datetime 

dates = [] 
for num in range(1,8): 
        today = datetime.date.today()
        days_ago = str(today - datetime.timedelta(days=(8-num)))
        days = days_ago.split("-")
        dates.append(days[1] + "/" + days[2])

