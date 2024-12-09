import streamlit as st
import pandas as pd
import os

# path
QUESTIONS_FILE = "questions.csv"

# Initialize
def initialize(file_path):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Email", "Question"])
        df.to_csv(file_path, index=False)
    return pd.read_csv(file_path)

# Save a new question to csv
def save_question(file_path, email, question):
    new_data = {"Email": email, "Question": question}
    df = pd.read_csv(file_path)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(file_path, index=False)

# use initialize
initialize(QUESTIONS_FILE)


#### content
st.header("How does UAC compare to the SLC campus?")
details = "The two experiences are hard to compare, as they are two completely different experiences! At UAC, you have the opportunity to be a part of a small student body with smaller, more specialized events. In SLC, the campus is much larger, creating a more spread out feeling."
st.write(details)

st.header("What made you decide to attend UAC?")
details = "I (Lucy) wanted the opportunity to study abroad and this opportunity presented itself! Because of the affordability, resources, and connection to the main campus, studying abroad at UAC opened up doors that may not have been opened up without the support from the main campus."
st.write(details)

st.header("What is your main mode of transportation?")
details = "The public transportation system in Korea is easy to navigate and super convenient. You can purchase a T-Money Card at most convenience stores. With a T-Money Card, you will want to load money onto the card and then you can tap on and off of every bus or subway. If you are looking to use a Taxi, the app Kakao Taxi allows you to book a taxi from wherever you are."
st.write(details)

st.header("How much is tuition at UAC for a student who is at the main campus full time?")
details = "The tuition at UAC is a flat rate of 10,000 USD for the first 17 credit hours taken, but students from the main campus automatically receive a scholarship of 5,000 USD to attend the Asia Campus for a semester. However, if you go over 17 credits, it is an additional 700 USD per credit. This fee does not include housing."
st.write(details)

st.header("Can I get an on-campus job without a work visa?")
details = "Yes! I (Lucy) worked two on campus jobs during my time at UAC. Students are able to work up to three jobs as long as they don't go over 20 hours a week. The pay for these jobs is through experiential learning scholarships that is applied to your tuition at the start of the semester. You can apply for these positions through handshake. Look up the University of Utah Asia Campus on handshake and the positions will be available. Hiring takes place at the end of the previous semester, so make sure to keep your eye out for important updates."
st.write(details)

# Questionaire
st.header("Have a question? Connect with us by entering your information below!")
with st.form("question_form"):
    email = st.text_input("Enter your Email")
    question = st.text_area("Enter your Question")
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if email and question:
            # Save the question to the CSV file
            save_question(QUESTIONS_FILE, email, question)
            st.success("Thank you for your question. We will respond as soon as possible.")
        else:
            st.error("Please fill out both fields before submitting!")

# admin Key is 1234

adminkey= st.text_input("enter admin key to view questions")

if adminkey =="1234": 
    st.subheader("Current Questions Submitted")
    if os.path.exists(QUESTIONS_FILE):
        submitted_questions = pd.read_csv(QUESTIONS_FILE)
        st.dataframe(submitted_questions)
    else:
        st.write("enter correct admin key")