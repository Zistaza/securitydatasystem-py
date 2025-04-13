Secure Data Encryption System 🔏🗝
This is a secure data storage and retrieval system built using Streamlit, where users can encrypt and store their data securely with a unique passkey. The system allows users to:

🔒 Store Encrypted Data: Users can input data and encrypt it with a passkey.

🔓 Retrieve Data: Users can decrypt previously stored data using the correct passkey.

🔑 Secure Login: Users need to log in to access and manage their encrypted data.

🚫 Lockout After Failed Attempts: Multiple failed login attempts trigger a lockout for a set period.

Features:
Secure storage of data using encryption (Fernet encryption).

Data retrieval and decryption by providing the correct passkey.

User authentication with a login system.

Protection against multiple failed login attempts with lockout duration.

Setup:
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Zistaza/securitydatasystem-py.git
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run securedataencrpt.py
Usage:
Register a new user: Enter a username and password.

Login: After successful registration, log in using the credentials.

Store Data: Enter your data, encrypt it, and save it securely.

Retrieve Data: Paste encrypted data and provide the correct passkey to decrypt
