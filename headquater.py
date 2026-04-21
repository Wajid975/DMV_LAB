import pandas as pd

data = [
    ["TCS", "Mumbai, Maharashtra"],
    ["Accenture", "Dublin"],
    ["Cognizant", "Teaneck, New Jersey"],
    ["ICICI Bank", "Mumbai, Maharashtra"],
    ["Wipro", "Bangalore/Bengaluru, Karnataka"],
    ["HDFC Bank", "Mumbai, Maharashtra"],
    ["Infosys", "Bengaluru/Bangalore, Karnataka"],
    ["Capgemini", "Paris"],
    ["Tech Mahindra", "Pune, Maharashtra"],
    ["Genpact", "New York, New York"],
    ["HCLTech", "Noida, Uttar Pradesh"],
    ["Axis Bank", "Mumbai, Maharashtra"],
    ["Concentrix", "Fremont, California"],
    ["IBM", "Armonk, New York"],
    ["Reliance Jio", "Navi Mumbai, Maharashtra"],
    ["Amazon", "Seattle, Washington"]
]


df = pd.DataFrame(data, columns=["Company", "HQ"])


print(df["HQ"])