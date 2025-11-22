from flask import Flask, request, jsonify
from flask_cors import CORS
from crypto_utils import *
import base64
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Generate RSA keys once
if not os.path.exists("rsa_keys"):
    os.makedirs("rsa_keys")

if not os.path.exists("rsa_keys/private.pem"):
    private, public = generate_rsa_keys()
    open("rsa_keys/private.pem", "wb").write(private)
    open("rsa_keys/public.pem", "wb").write(public)

private_key = open("rsa_keys/private.pem", "rb").read()
public_key = open("rsa_keys/public.pem", "rb").read()


@app.route("/encrypt", methods=["POST"])
def encrypt_message():
    data = request.json
    message = data["message"]

    aes_key = generate_aes_key()
    encrypted_msg = aes_encrypt(aes_key, message)
    encrypted_key = rsa_encrypt(public_key, aes_key)

    return jsonify({
        "aes_key_rsa_encrypted": base64.b64encode(encrypted_key).decode(),
        "encrypted_message": encrypted_msg.decode()
    })


@app.route("/decrypt", methods=["POST"])
def decrypt_message():
    data = request.json

    encrypted_key = base64.b64decode(data["aes_key_rsa_encrypted"])
    encrypted_msg = data["encrypted_message"].encode()

    aes_key = rsa_decrypt(private_key, encrypted_key)
    decrypted_msg = aes_decrypt(aes_key, encrypted_msg)

    return jsonify({"decrypted_message": decrypted_msg})


app.run(host="0.0.0.0", port=5000, debug=True)
