import plotly.express as px
import csv
import numpy as np

tvSize=[]
time=[]

with open("Student Marks vs Days Present.csv",newline="") as c:
    data=csv.DictReader(c)
    datalist=list(data)
    for row in data:
        tvSize.append(float(row["Marks In Percentage"]))
        time.append(float(row["Days Present"]))
        

print(time)
correlation=np.corrcoef(tvSize,time)
print(correlation[0,1])