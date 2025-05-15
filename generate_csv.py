import pandas as pd

data = {
    "Course_ID": [1, 2, 3, 4, 5],
    "Title": [
        "Python for Data Analysis",
        "Data Science with Python",
        "Excel for Data Analysis",
        "Statistics for Data Science",
        "SQL for Data Analytics"
    ],
    "Instructor": ["John Doe", "Jane Smith", "Alice Brown", "Bob Stone", "Diana Prince"],
    "Rating": [4.6, 4.7, 4.5, 4.4, 4.8],
    "Reviews": [1250, 980, 870, 765, 1560],
    "Students": [50000, 43000, 39000, 35000, 60000],
    "Price": [49, 39, 29, 35, 45]
}

df = pd.DataFrame(data)

df.to_csv("udemy_courses.csv", index=False)

print("CSV file 'udemy_courses.csv' created successfully!")
