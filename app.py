import streamlit as st
import google.generativeai as genai

# ---------------------------
# GEMINI API CONFIGURATION
# ---------------------------

API_KEY = "YOUR_API_KEY_HERE"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
# ---------------------------
# PAGE SETTINGS
# ---------------------------

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ AI Content Generator")
st.markdown("Generate Blogs and Social Media Captions using Gemini AI")

# ---------------------------
# USER INPUTS
# ---------------------------

topic = st.text_input(
    "Enter Topic"
)

content_type = st.selectbox(
    "Content Type",
    [
        "Blog Post",
        "Social Media Caption"
    ]
)

tone = st.selectbox(
    "Select Tone",
    [
        "Professional",
        "Casual",
        "Friendly",
        "Marketing",
        "Inspirational"
    ]
)

# ---------------------------
# GENERATE FUNCTION
# ---------------------------

def generate_content():

    prompt = f"""
    Generate a {content_type}
    on the topic: {topic}

    Tone: {tone}

    Make the content engaging,
    well structured,
    and easy to read.
    """

    response = model.generate_content(
        prompt
    )

    return response.text

# ---------------------------
# GENERATE BUTTON
# ---------------------------

if st.button("Generate Content"):

    if topic == "":

        st.warning(
            "Please enter a topic."
        )

    else:

        content = generate_content()

        st.subheader(
            "Generated Content"
        )

        st.write(content)

        word_count = len(
            content.split()
        )

        char_count = len(
            content
        )

        st.info(
            f"Word Count: {word_count}"
        )

        st.info(
            f"Character Count: {char_count}"
        )

# ---------------------------
# REGENERATE BUTTON
# ---------------------------

if st.button("Regenerate"):

    if topic != "":

        content = generate_content()

        st.subheader(
            "Regenerated Content"
        )

        st.write(content)

        word_count = len(
            content.split()
        )

        char_count = len(
            content
        )

        st.info(
            f"Word Count: {word_count}"
        )

        st.info(
            f"Character Count: {char_count}"
        )