import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Login Website (No Protection)",
    layout="centered"
)

# ---------------- USER CREDENTIALS ----------------
CREDENTIALS = {
    "naveen": "0067",
    "aadhish": "0069"
}

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "attack_running" not in st.session_state:
    st.session_state.attack_running = False

# ---------------- TITLE ----------------
st.markdown("## 🔓 Login Website (No Protection)")
st.caption(
    "This page demonstrates how brute-force attacks succeed when no security is applied."
)

# ---------------- LOGIN FORM ----------------
username = st.text_input("Username")

col1, col2 = st.columns([5, 1])

with col1:
    password = st.text_input("Password (4 digits)", type="password")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🐞"):
        st.session_state.attack_running = True

st.caption("🐞 Click the bug icon to simulate a brute-force attack")

# ---------------- NORMAL LOGIN ----------------
if st.button("Login"):
    if username in CREDENTIALS and password == CREDENTIALS[username]:
        st.session_state.logged_in = True
    else:
        st.error("❌ Invalid username or password")

# ---------------- BRUTE FORCE SIMULATION ----------------
if st.session_state.attack_running and not st.session_state.logged_in:
    st.warning("⚠ Brute-force attack in progress (bot behavior)")

    if username in CREDENTIALS:
        correct_password = CREDENTIALS[username]

        for i in range(10000):
            attempt = str(i).zfill(4)
            st.write(f"Trying password: **{attempt}**")

            # No delay → insecure system
            if attempt == correct_password:
                st.success(f"Password cracked by bot: {attempt}")
                st.session_state.logged_in = True
                st.session_state.attack_running = False
                break
    else:
        st.error("❌ Username not found. Bot attack failed.")
        st.session_state.attack_running = False

# ---------------- ACCESS GRANTED CONTENT ----------------
if st.session_state.logged_in:
    st.success("✅ Access Granted")

    st.markdown("### 📄 Brute Force Attack – Awareness Resources")

    # ---- PDF SECTION ----
    pdf_path = os.path.join(os.path.dirname(__file__), "brute_force.pdf")

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()

        st.download_button(
            label="📥 Download Brute Force Attack PDF",
            data=pdf_data,
            file_name="brute_force_attack_awareness.pdf",
            mime="application/pdf"
        )
    else:
        st.error("PDF file not found. Please upload brute_force.pdf.")

    # ---- ARTICLE LINK ----
    st.markdown(
        "🔗 **Read our article:** "
        "[Brute Force Attack – Explained](https://bruteforce-attack-explained.blogspot.com/2026/01/brute-force-attack.html)"
    )

    st.markdown("---")
    st.caption("Team THUNDER (Naveen, Aadhish) • Educational demo only")
