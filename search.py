import pandas as pd

# Load the Excel file containing jobs data
jobs_df = pd.read_excel("jobs.xlsx")
# Load the Excel file containing courses data
courses_df = pd.read_excel("courses.xlsx")


def search_jobs(location):
    result = jobs_df[jobs_df['Location'].str.contains(location, case=False)]
    return result

def search_courses(language):
    result = courses_df[courses_df['Language'].str.contains(language, case=False)]
    return result

# Function to search jobs based on location
#line of code 
# def search_jobs(location):
#     result = jobs_df[jobs_df['Location'].str.contains(location, case=False)]
#     return result





# # Function to search courses based on programming language
# def search_courses(language):
#     result = courses_df[courses_df['Language'].str.contains(language, case=False)]
#     return result


