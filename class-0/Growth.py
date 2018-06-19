from matplotlib import pyplot as plt 
import pandas as pd 
data = pd.read_csv("countries.csv")
india = data[data.country == "India"]
china = data[data.country == "China"]
usa = data[data.country == "United States"]
plt.plot(india.year,india.population/india.population.iloc[0]*100)
plt.plot(china.year,china.population/china.population.iloc[0]*100)
plt.plot(usa.year,usa.population/usa.population.iloc[0]*100)
plt.title("Population growth India vs China")
plt.xlabel("Years")
plt.ylabel("Population Growth")
plt.legend(["India","China","Usa"])
plt.show()
