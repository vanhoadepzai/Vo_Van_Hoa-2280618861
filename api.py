from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher 

app = Flask(__name__)

# Tạo đối tượng CaesarCipher
caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    cipher_text = data.get('plain_text')
    key = data.get('key')

    if cipher_text is None or key is None:
        return jsonify({'error': 'Missing cipher_text or key'}), 400

    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    encrypted_text = caesar_cipher.encrypt(cipher_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if cipher_text is None or key is None:
        return jsonify({'error': 'Missing cipher_text or key'}), 400

    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    decrypted_text = caesar_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
