import pandas as pd 
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.pie(df, values = "InternetUsers", names = "Country")
fig.show()