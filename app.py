import streamlit as st

st.set_page_config(page_title="VTU SGPA Calculator")

st.title("VTU 3rd Semester SGPA Calculator")

subjects = {
    "Mathematics": 4,
    "Data Structures": 3,
    "Digital design and Computer Organization": 4,
    "os": 4,
    "Data Structures Lab": 1,
    "oop": 3
}

def get_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 55:
        return 6
    elif marks >= 50:
        return 5
    else:
        return 0

total_credits = 0
total_points = 0

st.header("Enter Your Marks")

for subject, credit in subjects.items():
    marks = st.number_input(f"{subject} (Credits: {credit})", 0, 100)
    grade_point = get_grade_point(marks)
    total_points += grade_point * credit
    total_credits += credit

if st.button("Calculate SGPA"):
    sgpa = total_points / total_credits
    st.success(f"Your SGPA is: {round(sgpa, 2)}")
