import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Missing GEMINI_API_KEY in .env")
    st.stop()

# -----------------------------
# INIT CLIENT (NEW SDK)
# -----------------------------
client = genai.Client(api_key=api_key)

# -----------------------------
# RISK METER
# -----------------------------
def render_risk_meter(text):
    text = text.upper()

    st.markdown("### 🛡️ Risk Meter")

    if "CRITICAL" in text:
        st.error("🔴 CRITICAL RISK")
        st.progress(1.0)

    elif "HIGH" in text:
        st.warning("🟠 HIGH RISK")
        st.progress(0.75)

    elif "MEDIUM" in text:
        st.info("🟡 MEDIUM RISK")
        st.progress(0.5)

    elif "LOW" in text:
        st.success("🟢 LOW RISK")
        st.progress(0.25)

    else:
        st.info("⚪ UNKNOWN RISK")
        st.progress(0.1)

# -----------------------------
# UI
# -----------------------------
st.set_page_config(
    page_title="YahuuDot Lite",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ YahuuDot Lite")
st.subheader("AI Fraud Investigation Agent")

user_input = st.text_area(
    "Enter suspicious content:",
    height=220
)

# -----------------------------
# ANALYZE
# -----------------------------
if st.button("🚨 Analyze Threat"):

    if not user_input.strip():
        st.warning("Enter content first.")

    else:

        prompt = f"""
You are a cybersecurity fraud analyst.

Analyze for:
- phishing
- impersonation
- urgency tricks
- credential theft
- social engineering
- malicious links

Return:

## Threat Summary
## Risk Score (LOW / MEDIUM / HIGH / CRITICAL)
## Indicators
## Recommendations

Content:
{user_input}
"""

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success("Analysis Complete")
            st.markdown(response.text)

            render_risk_meter(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")