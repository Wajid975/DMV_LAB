import pandas as pd
import plotly.express as px


data = [
    ["TCS", 59900],
    ["Accenture", 38300],
    ["Cognizant", 34900],
    ["ICICI Bank", 28500],
    ["Wipro", 28400],
    ["HDFC Bank", 27800],
    ["Infosys", 26100],
    ["Capgemini", 24400],
    ["Tech Mahindra", 22800],
    ["Genpact", 22100],
    ["HCLTech", 21700],
    ["Axis Bank", 18700],
    ["Concentrix", 17600],
    ["IBM", 17400],
    ["Reliance Jio", 16900],
    ["Amazon", 16700]
]


df = pd.DataFrame(data, columns=["Company", "Reviews"])

df = df.sort_values(by="Reviews", ascending=False)

fig = px.funnel(df, x="Reviews", y="Company")

fig.update_layout(title="Company Reviews Funnel Chart")

fig.show()