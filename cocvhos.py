import csv
import numpy as np
import plotly.express as px
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Cup of coffee", y="Hours of sleep")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Cup_of_coffee"]))
            days_present.append(float(row["Hours_of_sleep"]))

    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Cup of coffee and Hours of sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/cups of coffee vs hours of sleep.csv"
    
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
