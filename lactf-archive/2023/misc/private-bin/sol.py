import json, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b"3cVSg0HRNq8SmAezph2ZBDl6B4WeEcAg"

with open("1cca80be-1b8a-4837-bdb1-cb56199e6cd7.json") as f:
    data = json.load(f)

for i, file in enumerate(data["files"]):
    try:
        raw = base64.b64decode(file["content"])
        iv = raw[:16]
        ciphertext = raw[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), 16)
        with open(f"output_{i}.bin", "wb") as f:
            f.write(plaintext)
        print(f"Saved output_{i}.bin ({len(plaintext)} bytes)")
    except Exception as e:
        print(f"Error {i}:", e)
