import pandas as pd 
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.histogram(df, x = "Country", y = "Population", color = "Country")
fig.show()