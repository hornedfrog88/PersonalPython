import json
import time
from pprint import pprint
#LOAD THE DATA
with open('C:/Users/Richard/OneDrive/Rich Files/Python/PersonalPython/d3_stats.json') as data_file:    
    data = json.load(data_file)
#CONVERT THE NUMERICAL WEEK VALUE TO STRING & INSERT THAT VALUE INTO THE ARRAY
for x in range(0,52):
    numericalweek = data[x]['week']
    convertedweekdate = time.strftime("%D %H:%M", time.localtime(int(numericalweek)))
    data[x]['convertweek'] = convertedweekdate
initialmax = data[0]['total']
weekindex = 0
#FIND THE WEEK THAT HAD THE MAXIMUM TOTAL VALUE-COMMITS
for y in range(1,52):
    if initialmax < data[y]['total']:
        initialmax = data[y]['total']
        weekindex = y
print(data[weekindex]['convertweek']) 