from cryptography.fernet import Fernet
import json
from flask import current_app, jsonify

def hash_code(data):
    try:
        data = json.dumps(data) if type(data) != str else data
        fernet = Fernet(current_app.config["KEY_HASHCODE"])
        encoded_str = fernet.encrypt(data.encode())
        return json.dumps(encoded_str.decode("utf-8"))
    except:
        pass
    
    return "Error!!!!"