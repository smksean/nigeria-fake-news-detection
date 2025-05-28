import streamlit as st
import joblib

# Load model and vectorizer (FIXED paths using raw strings)
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("vectorizer/vectorizer.pkl")

# Define news sources
sources = sorted([
    'ICIR Nigeria', 'Peoples Gazette', 'The Nation', 'GistReel', 'Leadership',
    'TV Continental', 'Daily Nigerian', 'Pulse NG', 'PM News', 'Eagle Online',
    'Tribune', 'TheCable', 'Blueprint', 'Vanguard', 'AIT', 'Naija News',
    'Linda Ikeji Blog', 'Zagazola Makama', 'Metro Watch', 'BellaNaija', 'Punch',
    'Arise News', 'Nairametrics', 'Independent NG', 'Sahara Reporters', 'Dubawa',
    'Tori NG', 'Africa Check', 'The Sun', 'YNaija', 'Politics Nigeria',
    'Channels TV', 'City People', 'FactCheckHub', 'ThisDay', 'NewsWireNGR',
    'Orient Daily', 'Naijaloaded', 'Opera News', 'Ripples Nigeria',
    'Guardian Nigeria', 'Premium Times', 'Daily Trust', 'Nigerian Tribune',
    'Nigerian Bulletin', '360Nobs', 'NAN', 'Legit NG', 'BusinessDay'
])

# Set up the page
st.set_page_config(page_title="Nigeria Fake News Detection", layout="centered")

# App Title with Design
st.markdown("<h1 style='text-align: center; color: green;'>🇳🇬 Nigeria Fake News Detection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>🔍 Detect if a news headline is real or fake based on the source</p>", unsafe_allow_html=True)

# Brief Guidelines
with st.expander("ℹ️ How it works"):
    st.markdown("""
    - **Step 1:** Enter the headline of a news article.
    - **Step 2:** Select the source it came from (e.g., Punch, Vanguard, Sahara Reporters).
    - **Step 3:** Click **Predict** to find out if the news is **Real** 🟢 or **Fake** 🔴.
    - Powered by a machine learning model trained on real-world Nigerian news sources.
    """)

# Input Section
st.subheader("📝 Enter News Information")
headline = st.text_input("Headline", "")
source = st.selectbox("News Source", sources)

# Prediction
if st.button("🔎 Predict"):
    if headline.strip() == "":
        st.warning("Please enter a headline to analyze.")
    else:
        input_text = f"{headline} {source}"
        input_vector = vectorizer.transform([input_text])
        prediction = model.predict(input_vector)[0]
        label = "🟢 Real" if prediction.lower() == "real" else "🔴 Fake"
        st.success(f"### Prediction: {label}")
