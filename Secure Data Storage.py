# data_source.py
from cryptography.fernet import Fernet

class DataSource:
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key
        self.objects = {
            1: {'id': 1, 'name': 'Object1', 'owner_id': self._encrypt('100')},
            2: {'id': 2, 'name': 'Object2', 'owner_id': self._encrypt('200')},
            # Add more objects here
        }

    def _encrypt(self, data):
        cipher_suite = Fernet(self.encryption_key)
        encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
        return encrypted_data

    def _decrypt(self, encrypted_data):
        cipher_suite = Fernet(self.encryption_key)
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
        return decrypted_data

    def get_object_by_id(self, obj_id):
        obj = self.objects.get(obj_id)
        if obj:
            obj['owner_id'] = self._decrypt(obj['owner_id'])
        return obj
