import time
import streamlit as st
from crypto_utils import hash_passkey, encrypt_data, decrypt_data, initialize_session, save_data

# Initialize cipher and session state
cipher = initialize_session()

# Main app interface
st.title("🔒 Secure Data Encryption System")

# Navigation menu
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu, key="page")

# Handle redirects (e.g., after login or failed attempts)
if st.session_state.redirect_to:
    choice = st.session_state.redirect_to
    st.session_state.redirect_to = None
    st.rerun()  # Updated from st.experimental_rerun()

if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.write("Store and retrieve data securely with a passkey.")

elif choice == "Store Data":
    st.subheader("📂 Store Data")
    st.write("Enter your data and a passkey. Save the encrypted text to retrieve it later!")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")
    if st.button("Encrypt & Save"):
        if user_data and passkey:
            encrypted_text = encrypt_data(user_data, cipher)
            salt, hashed_passkey = hash_passkey(passkey)
            st.session_state.stored_data[encrypted_text] = {"salt": salt, "hashed_passkey": hashed_passkey}
            save_data(st.session_state)
            st.success("✅ Data stored!")
            st.write("Copy this encrypted text:")
            st.code(encrypted_text)
            print(f"Stored data: {st.session_state.stored_data}")  # Debug storage
        else:
            st.error("⚠️ Fill in both fields!")

elif choice == "Retrieve Data":
    if st.session_state.failed_attempts >= 3:
        st.session_state.redirect_to = "Login"
        st.rerun()  # Updated from st.experimental_rerun()
    else:
        st.subheader("🔍 Retrieve Data")
        st.write("Paste the encrypted text and enter your passkey.")
        encrypted_text = st.text_area("Enter Encrypted Data:").strip()  # Trim whitespace
        passkey = st.text_input("Enter Passkey:", type="password")
        if st.button("Decrypt"):
            if encrypted_text and passkey:
                decrypted_text = decrypt_data(encrypted_text, passkey, cipher, st.session_state)
                if decrypted_text:
                    st.success(f"✅ Decrypted Data: {decrypted_text}")
                else:
                    st.error(f"❌ Wrong passkey! Attempts left: {3 - st.session_state.failed_attempts}")
            else:
                st.error("⚠️ Fill in both fields!")

elif choice == "Login":
    st.subheader("🔑 Login")
    login_pass = st.text_input("Master Password:", type="password")
    if st.button("Login"):
        if login_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.redirect_to = "Retrieve Data"
            st.success("✅ Success! Going back...")
            time.sleep(1.5)  # Delay to show the message
            st.rerun()  # Updated from st.experimental_rerun()
        else:
            st.error("❌ Wrong password!")