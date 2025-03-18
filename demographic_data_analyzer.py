import pandas as pd

def demographic_data_analyzer():
    # Read dataset
    df = pd.read_csv("adult.data.csv")
    
    # Number of people of each race
    race_count = df['race'].value_counts()
    
    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # Higher education (Bachelors, Masters, Doctorate)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    
    # Percentage of people with advanced education making >50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    
    # Percentage of people without advanced education making >50K
    lower_education_rich = round((df[~higher_education]['salary'] == '>50K').mean() * 100, 1)
    
    # Minimum work hours per week
    min_work_hours = df['hours-per-week'].min()
    
    # Percentage of min-hour workers earning >50K
    min_workers = df['hours-per-week'] == min_work_hours
    rich_percentage = round((df[min_workers]['salary'] == '>50K').mean() * 100, 1)
    
    # Country with highest percentage of >50K earners
    country_salary_ratio = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_salary_ratio.idxmax()
    highest_earning_country_percentage = round(country_salary_ratio.max() * 100, 1)
    
    # Most popular occupation for >50K earners in India
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
    top_IN_occupation = india_occupation.idxmax()
    
    # Results dictionary
    results = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    
    return results

if __name__ == "__main__":
    result = demographic_data_analyzer()
    for key, value in result.items():
        print(f"{key}: {value}")
