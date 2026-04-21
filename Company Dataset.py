import pandas as pd
import matplotlib.pyplot as plt


companies = ["TCS","Accenture","Cognizant","ICICI Bank","Wipro",
             "HDFC Bank","Infosys","Capgemini","Tech Mahindra",
             "Genpact","HCLTech","Axis Bank","Concentrix",
             "IBM","Reliance Jio","Amazon"]

ratings = [3.8,4.1,3.9,4.0,3.9,3.9,3.9,3.9,3.7,4.0,3.8,3.9,4.0,4.1,4.0,4.2]

reviews = [59900,38300,34900,28500,28400,27800,26100,24400,
           22800,22100,21700,18700,17600,17400,16900,16700]

employees = [100000,100000,100000,100000,100000,100000,100000,100000,
             100000,100000,100000,75000,30000,75000,75000,100000]

hq = ["Mumbai","Dublin","Teaneck","Mumbai","Bengaluru",
      "Mumbai","Bengaluru","Paris","Pune","New York",
      "Noida","Mumbai","Fremont","Armonk","Navi Mumbai","Seattle"]

pie_companies = ["TCS","Accenture","Cognizant","Wipro","Infosys"]
years = [55,34,29,78,42]

fig, axs = plt.subplots(2, 3, figsize=(18,10))

axs[0,0].bar(companies, ratings, color="skyblue")
axs[0,0].set_title("Company Ratings")

axs[0,1].plot(companies, employees, marker='o', color='green')
axs[0,1].set_title("Employee Count")
axs[0,1].tick_params(axis='x', rotation=45)
axs[0,2].pie(years, labels=pie_companies, autopct='%1.1f%%', startangle=140)
axs[0,2].set_title("Company Age Distribution")

sorted_data = sorted(zip(companies, reviews), key=lambda x: x[1], reverse=True)
comp_sorted, rev_sorted = zip(*sorted_data)

axs[1,0].barh(comp_sorted, rev_sorted, color="orange")
axs[1,0].invert_yaxis()
axs[1,0].set_title("Company Reviews")


axs[1,1].axis('off') 
table_data = list(zip(companies, hq))

table = axs[1,1].table(cellText=table_data,
                       colLabels=["Company", "HQ"],
                       loc='center')

table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.2)

axs[1,1].set_title("Company Headquarters")

axs[1,2].axis('off')

plt.tight_layout()
plt.show()