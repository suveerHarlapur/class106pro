import csv,numpy as np,plotly_express as px

def getDataSource():
    days = []
    marks = []
    with open('present.csv') as f:
        filedata = csv.DictReader(f)
        
        for row in filedata:
            days.append(float(row['Days Present']))
            marks.append(float(row['Marks In Percentage']))
    return{"x":days,"y":marks}
def fig():
    with open("present.csv") as fd:
        file = csv.DictReader(fd)
        fig = px.scatter(file,x='Days Present',y='Marks In Percentage')
        fig.show()
def corelation():
    data = getDataSource()
    correlation = np.corrcoef(data['x'],data['y'])
    print(correlation[0,1])

corelation()
fig()
