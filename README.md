🔒 Secure Data Encryption System
A super dope web app built with Python and Streamlit to encrypt and decrypt secret messages securely. It’s like a digital vault for your data, with extra security features to keep hackers out. 🛡️
✨ Features

Encrypt & Store: Type a message and a passkey to encrypt it into a secret code.
Decrypt & Retrieve: Paste the code and enter the passkey to get your message back.
Lockout System: Get locked out after 3 wrong passkey tries. Use the master password (admin123) to get back in.
Data Persistence: Saves encrypted data to data.json so it’s there even after you close the app.
Advanced Security: Uses PBKDF2 (way stronger than SHA-256) to protect passkeys.

🚀 Bonus Challenges Completed

Data Persistence: Stores data in a JSON file instead of memory.
Advanced Security: Uses PBKDF2 hashing for passkeys.

🛠️ Setup
Prerequisites

Python 3.7 or higher (download from python.org).
A terminal (Command Prompt or PowerShell on Windows).

Installation

Clone or download this project to a folder (e.g., secure_data_encryption_a).
Open a terminal and navigate to the folder:cd path/to/secure_data_encryption_a


Install the required libraries:pip install -r requirements.txt



Running the App

In the terminal, run:streamlit run app.py


Your browser should open to http://localhost:8501. If not, go there manually.

📖 How to Use

Store Data:
Go to "Store Data" in the sidebar.
Type a message (e.g., "Hello") and a passkey (e.g., "mysecret").
Click "Encrypt & Save".
Copy the encrypted text (starts with gAAAAAB...).


Retrieve Data:
Go to "Retrieve Data".
Paste the encrypted text and enter the passkey.
Click "Decrypt" to see your message.
If you enter the wrong passkey 3 times, you’ll go to the "Login" page.


Login:
On the "Login" page, enter the master password: admin123.
Click "Login" to go back to "Retrieve Data".
Wrong password? You’ll see an error.



📂 Project Structure

app.py: The web interface (buttons, text boxes, etc.).
crypto_utils.py: The logic (encryption, decryption, saving data).
requirements.txt: Lists the libraries needed.
data.json: Where encrypted data is saved (created when you store data).

🔐 Security Notes

Encryption: Uses Fernet from the Cryptography library for strong encryption.
Passkeys: Protected with PBKDF2, which adds a random salt and hashes 100,000 times.
Master Password: Hardcoded as admin123 for demo purposes. In a real app, it’d be stored securely.

🐛 Troubleshooting

Wrong passkey error: Make sure you copy the encrypted text exactly (no extra spaces). Reset by deleting data.json and restarting.
App not running: Check Python and libraries are installed. Run pip install -r requirements.txt again.
No success message on login: The app redirects after 1.5 seconds to show the message. If it’s too fast, increase the time.sleep(1.5) in app.py.

🙌 Acknowledgments
Built as part of the Panaversity Learn Modern AI Python course. Shoutout to my coding journey for making this lit! 🔥
