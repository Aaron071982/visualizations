import pandas as pd 
data = [1,2,3,4,5]
import plotly.express as px

df = pd.read_csv("line_chart.csv")
# df = pd.DataFrame(data)
# print(df)

fig = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per Capita Income")
fig.show()

