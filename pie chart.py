import matplotlib.pyplot as plt


companies = ["TCS", "Accenture", "Cognizant", "Wipro", "Infosys"]
years = [55, 34, 29, 78, 42]


plt.figure(figsize=(6,6))
plt.pie(
    years,
    labels=companies,
    autopct='%1.1f%%',
    startangle=140
)

plt.title("Company Age Distribution (Years)")

plt.show()