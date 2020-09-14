import plotly.express as px
import csv
import numpy as np
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Size of TV", y="Average time spent watching TV in a week")
        fig.show()

def getDataSource(data_path):
    Size_of_TV = []
    avgTime= []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Size_of_TV.append(float(row["Size of TV"]))
            avgTime.append(float(row["Average time spent watching TV in a week"]))

    return {"x" : Size_of_TV, "y": avgTime}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size vs Time :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Size of TV,_Average time spent watching TV in a week (hours).csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()