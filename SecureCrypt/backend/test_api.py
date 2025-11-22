import requests

BASE_URL = "http://127.0.0.1:5000"

def test_encrypt_decrypt():
    message = "Test message from Python script"

    # Test encryption
    encrypt_resp = requests.post(f"{BASE_URL}/encrypt", json={"message": message})
    assert encrypt_resp.status_code == 200, f"Encryption failed: {encrypt_resp.text}"
    data = encrypt_resp.json()
    enc_key = data["aes_key_rsa_encrypted"]
    enc_msg = data["encrypted_message"]
    print("Encryption successful.")
    print(f"Encrypted Message: {enc_msg}")
    print(f"Encrypted AES Key: {enc_key}")

    # Test decryption
    decrypt_resp = requests.post(f"{BASE_URL}/decrypt", json={
        "aes_key_rsa_encrypted": enc_key,
        "encrypted_message": enc_msg
    })
    assert decrypt_resp.status_code == 200, f"Decryption failed: {decrypt_resp.text}"
    decrypted_message = decrypt_resp.json()["decrypted_message"]
    print("Decryption successful.")
    print(f"Decrypted Message: {decrypted_message}")

    assert decrypted_message == message, "Decrypted message does not match original"

if __name__ == "__main__":
    test_encrypt_decrypt()
