import pandas as pd
import matplotlib.pyplot as plt

data = [
    ["TCS", 100000],
    ["Accenture", 100000],
    ["Cognizant", 100000],
    ["ICICI Bank", 100000],
    ["Wipro", 100000],
    ["HDFC Bank", 100000],
    ["Infosys", 100000],
    ["Capgemini", 100000],
    ["Tech Mahindra", 100000],
    ["Genpact", 100000],
    ["HCLTech", 100000],
    ["Axis Bank", 75000],
    ["Concentrix", 30000],
    ["IBM", 75000],
    ["Reliance Jio", 75000],
    ["Amazon", 100000]
]


df = pd.DataFrame(data, columns=["Company", "Employees"])

plt.figure(figsize=(12,6))
plt.plot(df["Company"], df["Employees"], marker='o', linestyle='-', color='green')

plt.xlabel("Company")
plt.ylabel("Number of Employees")
plt.title("Company Employee Count Comparison")

plt.xticks(rotation=45)

for i, v in enumerate(df["Employees"]):
    plt.text(i, v + 2000, str(v), ha='center')

plt.tight_layout()
plt.show()