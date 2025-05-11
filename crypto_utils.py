import hashlib
import os
import json
from cryptography.fernet import Fernet
import streamlit as st

def hash_passkey(passkey):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt, 100000).hex()
    return salt.hex(), hashed

def verify_passkey(passkey, stored_salt, stored_hashed):
    salt = bytes.fromhex(stored_salt)
    hashed = hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt, 100000).hex()
    return hashed == stored_hashed

def encrypt_data(text, cipher):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey, cipher, session_state):
    print(f"Checking encrypted_text: {encrypted_text}")
    if encrypted_text in session_state.stored_data:
        stored = session_state.stored_data[encrypted_text]
        print(f"Stored data found: {stored}")
        if verify_passkey(passkey, stored["salt"], stored["hashed_passkey"]):
            session_state.failed_attempts = 0
            print("Passkey verified successfully!")
            try:
                return cipher.decrypt(encrypted_text.encode()).decode()
            except Exception as e:
                print(f"Decryption failed: {e}")
                return None
        else:
            print("Passkey verification failed!")
    else:
        print("Encrypted text not found in stored_data!")
    session_state.failed_attempts += 1
    return None

def save_data(session_state):
    data_to_save = {
        "key": session_state.key.decode(),
        "stored_data": session_state.stored_data
    }
    with open("data.json", "w") as f:
        json.dump(data_to_save, f)

def load_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            return data.get("key", Fernet.generate_key().decode()), data.get("stored_data", {})
    except FileNotFoundError:
        return Fernet.generate_key().decode(), {}

def initialize_session():
    if 'key' not in st.session_state:
        key, stored_data = load_data()
        st.session_state.key = key.encode()
        st.session_state.stored_data = stored_data
    if 'failed_attempts' not in st.session_state:
        st.session_state.failed_attempts = 0
    if 'redirect_to' not in st.session_state:
        st.session_state.redirect_to = None
    return Fernet(st.session_state.key)