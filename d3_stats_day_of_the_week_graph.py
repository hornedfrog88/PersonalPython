import matplotlib.pyplot as plt
import json
from pprint import pprint
#LOAD THE DATA
with open('C:/Users/Richard/OneDrive/Rich Files/Python/PersonalPython/d3_stats.json') as data_file:    
    data = json.load(data_file)
SundayTotal = 0
MondayTotal = 0
TuesdayTotal = 0
WednesdayTotal = 0
ThursdayTotal = 0
FridayTotal = 0
SaturdayTotal = 0
for k in range(0,52):
    daysoftheweek = data[k]['days']
    SundayTotal = SundayTotal + daysoftheweek[0]
    MondayTotal = MondayTotal + daysoftheweek[1]
    TuesdayTotal = TuesdayTotal + daysoftheweek[2]
    WednesdayTotal = WednesdayTotal + daysoftheweek[3]
    ThursdayTotal = ThursdayTotal + daysoftheweek[4]
    FridayTotal = FridayTotal + daysoftheweek[5]
    SaturdayTotal = SaturdayTotal + daysoftheweek[6]
days = [0,1,2,3,4,5,6]
counts = [SundayTotal,MondayTotal,TuesdayTotal,WednesdayTotal,ThursdayTotal,FridayTotal,SaturdayTotal]
labels = ['Sun','Mon','Tues','Wed','Thur','Fri','Sat']
plt.ylabel('Number of Commits')
plt.xlabel('Day of the Week')
plt.bar(days,counts,align = 'center')
plt.xticks(x, labels)
plt.show()