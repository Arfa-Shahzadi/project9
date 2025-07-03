#project 9 Build a python website in 15 minutes with streamlit

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title= "Student Data Generator", layout="wide")
st.title("Student CSV File Generator")

names = ["Ali", "Aisha", "Ahmed", "Fatima", "Usman", "Zainab", "Bilal", "Hina", "Sami", "Hadia", 
         "Hamza", "Sara", "Tariq", "Mehak", "Faisal"]

students = []
for i in range(1,16):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25), 
        "Grade": random.choice(["A","B","C","D","E","F"]),
        "Marks": random.radiant(40,100)
    }
    students.append(student)


df = pd.DataFrame(students)
st.subheader("Generated Student Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")
st.success("Students Record Generated successfully!")
