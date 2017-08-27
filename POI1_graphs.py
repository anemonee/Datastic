import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime  
from datetime import timedelta  


def csvparser(path_datafile):
    df = pd.read_csv(path_datafile)
    df.Date = pd.to_datetime(df.Date, format = '%d/%m/%y')
    print df.dtypes
    parameter_list = []
    for i in df.Parameter:
        if i not in parameter_list:
            parameter_list.append(i)
    print "Parameters tested:"
    print parameter_list
    count = 1
    for i in parameter_list:
        dfi = df[df["Parameter"] == i]
        parametergraph(dfi,i,count)
        count = count + 1
        
def parametergraph(dfT3, name, count):
    dfT3 = dfT3.sort_values('Date', ascending=True)
    plt.figure(name)
    plt.plot(dfT3['Date'], dfT3['Value'], marker = "*", color = 'blue')
    plt.plot(dfT3['Date'], dfT3['Low'], marker = 'o', color = 'green')
    plt.plot(dfT3['Date'], dfT3['High'], marker = 'o', color = 'green')

    plt.xticks(rotation='vertical')
    plt.legend()
    minlimx = min(dfT3['Date']) - timedelta(days = 100)
    maxlimx = max(dfT3['Date']) + timedelta(days = 100)
    minlimy = min(min(dfT3['Low']), min(dfT3['Value'])) 
    maxlimy = max(max(dfT3['High']), max(dfT3['Value']))
    jump = maxlimy/8 - minlimy/8
    plt.xlim(minlimx, maxlimx)
    plt.ylim(minlimy- jump, maxlimy + jump)
    plt.show()

    
csvparser('db/POI1_data.csv')

    
