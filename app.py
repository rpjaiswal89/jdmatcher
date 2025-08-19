import streamlit as st
from PyPDF2 import PdfReader
from rapidfuzz import fuzz


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

st.title("📄 JD Matcher App")
st.write("Upload a Job Description (JD) and a Resume to check score.")

# File uploaders
jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if jd_file and resume_file:
    # Extract text
    jd_text = extract_text_from_pdf(jd_file)
    resume_text = extract_text_from_pdf(resume_file)

    # Calculate similarity
    score = fuzz.token_set_ratio(jd_text, resume_text)

    st.subheader("✅ Match Score")
    st.metric("Similarity", f"{score}%")

    # Display extra info
    st.subheader("Job Description Extract")
    st.text_area("JD Content", jd_text[:1000], height=200)

    st.subheader("Resume Extract")
    st.text_area("Resume Content", resume_text[:1000], height=200)