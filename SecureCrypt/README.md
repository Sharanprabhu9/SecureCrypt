# SecureCrypt – Hybrid Encryption Web App (AES + RSA)

## Project Overview

SecureCrypt is a hybrid encryption web application combining AES and RSA encryption algorithms for secure message encryption and decryption. It features:

- Backend implemented in Python (Flask)
- AES + RSA hybrid encryption for improved security and performance
- Frontend user interface with HTML and TailwindCSS
- API endpoints for encrypting and decrypting messages
- Simple folder structure for easy navigation and maintenance
- Ready-to-run with installation steps and explanations

---

## Folder Structure

```
SecureCrypt/
│── backend/
│   ├── app.py
│   ├── rsa_keys/
│   │     ├── private.pem  # Generated on first run
│   │     └── public.pem   # Generated on first run
│   ├── crypto_utils.py
│   ├── requirements.txt
│
│── frontend/
│   ├── index.html
│   ├── style.css
│
└── README.md
```

---

## Installation and Running

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

This will start the Flask API server on `http://0.0.0.0:5000`.

### Frontend

Simply open `frontend/index.html` in your browser.

---

## How the Project Works

- User enters a message in the frontend.
- When "Encrypt" is clicked:
  - Frontend sends the message to the backend `/encrypt` endpoint.
  - Backend generates an AES key and encrypts the message.
  - AES key is encrypted with the RSA public key.
  - Backend returns both encrypted message and encrypted AES key.
- When "Decrypt" is clicked:
  - Frontend sends both encrypted data to `/decrypt`.
  - Backend decrypts AES key with RSA private key.
  - Then decrypts the message using AES.
  - Returns decrypted plaintext.

---

## Technical Explanation (for Viva)

### Why Hybrid Encryption?

- AES is fast symmetric encryption.
- RSA is slower but secure asymmetric encryption.
- Combining them offers best of both:
  - AES encrypts the actual message quickly.
  - RSA encrypts the AES key securely for key exchange.

### Real-World Applications

Hybrid encryption is used in popular apps like WhatsApp, Signal, banking apps, and HTTPS websites to balance speed and security.

---

## Extras Available

Say **"give report"**, **"give ppt"**, or others for supplementary materials like:

- PDF project report
- PPT for seminar
- UML and ER diagrams
- Code explanation notes
- GitHub-ready README

---

Your SecureCrypt project is now ready for use and presentation!
