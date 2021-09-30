import pandas as pd
import plotly.express as px

print(" Kyra is VERY lazy ! She works as an sports-science data visualizer. But she never completes her excel sheets manually! Her boss always complains about her. Will you help Kyra with her work by creating a simple Raw data to visualized data and automate the process of data visualization ?? If yes , come on!")
def BG():
    df=pd.read_csv('data.csv')
    fig=px.bar(df,x='team',y='hours_played')
    fig.show()

def SG():
    df=pd.read_csv('data.csv')
    fig=px.scatter(df,x='team',y='hours_played',size='players count',color='team',size_max=60,title="Info about PBL teams")
    fig.show()



print("What do you want to do (BAR, SCATTER , LINE)???")
opt=str(input('if you want to make a BAR press 1, If you want to make a scatter press 2 -> '))
if opt=='1':
    BG()
if opt=='2':
    SG()

