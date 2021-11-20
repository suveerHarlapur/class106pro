import csv,numpy as np,plotly_express as px
from re import X;
filedata = ''
def getDataSource():
    sleepinhr = []
    coffee = []
    with open('sleep.csv') as f:
        filedata = csv.DictReader(f)
        for row in filedata:
            sleepinhr.append(float(row['sleep in hour']))
            coffee.append(float(row['Coffee in ml']))
        return{'x':sleepinhr,'y':coffee}
def corelation():
    data = getDataSource()
    correlation = np.corrcoef(data['x'],data['y'])
    print(correlation[0,1])

def fig():
    with open("sleep.csv") as fd:
        file = csv.DictReader(fd)
        fig = px.scatter(file,x='sleep in hour',y='Coffee in ml')
        fig.show()
corelation()
fig()