import base64
import hashlib
import io
import json
import os

def encrypt_json(json_data, watermark):
    # Hash the watermark
    hash_watermark = hashlib.sha256(watermark.encode()).digest()

    # Generate the encryption key
    key = os.urandom(32)

    # Encrypt the data
    cipher = aes_ctr.new(key, hash_watermark)
    encrypted_data = cipher.encrypt(json_data.encode())

    # Encode the encrypted data to base64
    encoded_data = base64.b64encode(encrypted_data).decode()

    return encoded_data


def main():
    # Get the JSON data
    with open("data.json", "r") as f:
        json_data = json.load(f)

    # Get the watermark
    watermark = "My secret watermark"

    # Encrypt the JSON data
    encrypted_data = encrypt_json(json_data, watermark)

    # Print the encrypted data
    print(encrypted_data)


if __name__ == "__main__":
    main()
