# How to Use SecureCrypt - Hybrid Encryption Web App

This guide explains how to set up, run, and use the SecureCrypt app for hybrid AES + RSA encryption and decryption.

---

## Prerequisites

- Python 3 installed on your system
- Internet Browser (Chrome, Firefox, Edge, etc.)

---

## Setup and Run Backend

1. Open a terminal/command prompt.
2. Navigate to the backend directory:
   ```
   cd SecureCrypt/backend
   ```
3. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Start the Flask backend server:
   ```
   python app.py
   ```
5. The server will start listening at `http://0.0.0.0:5000`.

---

## Use Frontend

1. Open the `SecureCrypt/frontend/index.html` file using your browser. You can open it directly without any server.
2. In the page, enter the message you want to encrypt in the textarea.
3. Click the **Encrypt** button. The encrypted message and the RSA-encrypted AES key will display below.
4. Click the **Decrypt** button to decrypt the message back to plain text.
5. You can repeat the process with other messages.

---

## Notes

- Ensure the backend server is running and accessible at `http://127.0.0.1:5000` for the frontend to work properly.
- The frontend and backend communicate via HTTP requests; they must run on the same machine or network.
- CORS is enabled in the backend to allow cross-origin requests from the frontend.

---

## Troubleshooting

- If the frontend does not respond or shows errors, check that the backend server is running.
- Make sure firewall or antivirus is not blocking communication on port 5000.
- For further assistance, consult the README.md or contact the author.

---

Enjoy secure messaging with SecureCrypt!
