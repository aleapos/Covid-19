import pandas as pd
import mysql.connector

csv = pd.read_csv("covid_data.csv")
csv = pd.DataFrame(csv)


data = csv.loc[:, ['continent','location','date','total_cases', 'new_cases' ,'total_deaths',
                   'new_deaths','total_tests', 'new_tests','positive_rate', 'tests_per_case', 'total_vaccinations', 'people_vaccinated',
                   'people_fully_vaccinated','new_vaccinations', 'hospital_beds_per_thousand','life_expectancy', 'population' ]]
data = data.fillna('0')
data = data.drop(data[data['continent'] == '0'].index)
print(data.head())
data.to_csv("covid_dataset.csv", index=False)