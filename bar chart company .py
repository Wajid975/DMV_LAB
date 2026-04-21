import pandas as pd
import matplotlib.pyplot as plt


data = [
    ["TCS", 3.8],
    ["Accenture", 4.1],
    ["Cognizant", 3.9],
    ["ICICI Bank", 4.0],
    ["Wipro", 3.9],
    ["HDFC Bank", 3.9],
    ["Infosys", 3.9],
    ["Capgemini", 3.9],
    ["Tech Mahindra", 3.7],
    ["Genpact", 4.0],
    ["HCLTech", 3.8],
    ["Axis Bank", 3.9],
    ["Concentrix", 4.0],
    ["IBM", 4.1],
    ["Reliance Jio", 4.0],
    ["Amazon", 4.2]
]


df = pd.DataFrame(data, columns=["Company", "Rating"])


df = df.sort_values(by="Rating", ascending=False)


plt.figure(figsize=(10,6))
plt.bar(df["Company"], df["Rating"], color="skyblue")

plt.xlabel("Company")
plt.ylabel("Rating")
plt.title("Company Ratings Comparison")


plt.xticks(rotation=45)

for i, v in enumerate(df["Rating"]):
    plt.text(i, v + 0.02, str(v), ha='center')

plt.tight_layout()
plt.show()