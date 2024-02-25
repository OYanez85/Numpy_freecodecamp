import pandas as pd

# Raw URL for the 'adult.data' file
url = 'https://raw.githubusercontent.com/OYanez85/Numpy_freecodecamp/develop/adult.data'

# Load the dataset
# Assuming the dataset does not contain a header row, we specify the column names manually
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                'hours-per-week', 'native-country', 'salary']

df = pd.read_csv(url, names=column_names, na_values=" ?", skipinitialspace=True)

# 1. How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()
print("People of each race represented in the dataset:\n", race_count)

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)
print("\nAverage age of men:", average_age_men)

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = ((df['education'] == 'Bachelors').mean() * 100).round(1)
print("\nPercentage of people who have a Bachelor's degree:", percentage_bachelors, "%")

# 4. What percentage of people with advanced education make more than 50K?
higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
rich_percentage = ((df[higher_education]['salary'] == '>50K').mean() * 100).round(1)
print("\nPercentage of people with advanced education making more than 50K:", rich_percentage, "%")

# 5. What percentage of people without advanced education make more than 50K?
lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
poor_percentage = ((df[lower_education]['salary'] == '>50K').mean() * 100).round(1)
print("\nPercentage of people without advanced education making more than 50K:", poor_percentage, "%")

# 6. What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()
print("\nMinimum number of hours a person works per week:", min_work_hours)

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage_min_hours = ((num_min_workers['salary'] == '>50K').mean() * 100).round(1)
print("\nPercentage of people working the minimum number of hours per week and making more than 50K:", rich_percentage_min_hours, "%")

# 8. What country has the highest percentage of people that earn >50K?
country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
highest_earning_country = country_earnings.idxmax()
highest_earning_country_percentage = (country_earnings.max() * 100).round(1)
print("\nCountry with the highest percentage of people earning >50K:", highest_earning_country)
print("Percentage of people in", highest_earning_country, "earning >50K:", highest_earning_country_percentage, "%")

# 9. Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
print("\nMost popular occupation for those who earn >50K in India:", top_IN_occupation)
