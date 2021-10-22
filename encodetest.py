# from base64 import b64encode, b64decode
# import hashlib
# from Cryptodome.Cipher import AES
# import os
# from Cryptodome.Random import get_random_bytes

# # salt = get_random_bytes(AES.block_size)
# # private_key = hashlib.scrypt('key'.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

# private_key = b'\xc7=\xb5h\xe6\xc4\x14\xcd\xdb\xbe\xea}\xbd}I\xd81g\r\xbbLSq\xb1$\x900%\xce\xbf\xc5\xa1'
# print('private_key', private_key)


# def encrypt(plain_text, private_key):
#     # generate a random salt
#     # salt = get_random_bytes(AES.block_size)

#     # use the Scrypt KDF to get a private key from the password
#     # private_key = hashlib.scrypt(
#     #     key.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

#     # create cipher config
#     cipher_config = AES.new(private_key, AES.MODE_GCM)
#     print('cipher_config', cipher_config)

#     # return a dictionary with the encrypted text
#     cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
#     return {
#         'cipher_text': b64encode(cipher_text).decode('utf-8'),
#         # 'salt': b64encode(salt).decode('utf-8'),
#         'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
#         'tag': b64encode(tag).decode('utf-8')
#     }


# def decrypt(enc_dict, private_key):
#     # decode the dictionary entries from base64
#     # salt = b64decode(enc_dict['salt'])
#     cipher_text = b64decode(enc_dict['cipher_text'])
#     nonce = b64decode(enc_dict['nonce'])
#     tag = b64decode(enc_dict['tag'])
    

#     # generate the private key from the password and salt
#     # private_key = hashlib.scrypt(
#     #     key.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

#     # create the cipher config
#     cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

#     # decrypt the cipher text
#     decrypted = cipher.decrypt_and_verify(cipher_text, tag)

#     return decrypted


# def main():
#     # key = input("key: ")
#     message = input("message: ")

#     # First let us encrypt secret message
#     encrypted = encrypt(message, private_key)
#     print(encrypted)

#     # Let us decrypt using our original password
#     decrypted = decrypt(encrypted, private_key)
#     print(bytes.decode(decrypted))

# main()




# 2 




# import base64
# import hashlib
# from Crypto.Cipher import AES
# from Crypto import Random
# import Crypto.Cipher
 
# BLOCK_SIZE = 16
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
# unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
# key = 'fde64urh23ikoaz849tjgt61yrhsfvbd'
# # iv = "5183666c72eec9e4".encode('utf-8')
# iv = b"5183666c72eec9e4"

# # random_var = 'sdploikjuhytregd'
 
# def encrypt(raw, password):
#     # private_key = hashlib.sha256(password.encode("utf-8")).digest()
#     private_key = 'bf3c199c2470cb477d907b1e0917c17b'
#     raw = pad(raw)
#     # iv = Random.new().read(AES.block_size)
#     cipher = AES.new(private_key, AES.MODE_CBC, iv)
#     return base64.b64encode(iv + cipher.encrypt(raw))
 
 
# def decrypt(enc, password):
#     # private_key = hashlib.sha256(password.encode("utf-8")).digest()
#     private_key = 'bf3c199c2470cb477d907b1e0917c17b'
#     enc = base64.b64decode(enc)
#     # iv = enc[:16]
#     cipher = AES.new(private_key, AES.MODE_CBC, iv)
#     return unpad(cipher.decrypt(enc[16:]))
 
 

# data = input("data: ")
# encrypted = encrypt(data, key)
# print('encrypted', encrypted)
 
# # encrypted = b'eGeISChbfWMajZkXdrQUSfSg0sdn68r/55CxwV2v88k='
# decrypted = decrypt(encrypted, key)
# print(bytes.decode(decrypted))



data = [
            {
                "name": "Hemal Moradiya",
                "email": "hemalmoradiya.ibl@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "flutter developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [
                        "device_token",
                        "device_token"
                    ],
                    "web": []
                }
            },
            {
                "name": "harshit",
                "email": "bhimaniharshit09904@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "flutter developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token"
                    ],
                    "web": []
                }
            },
            {
                "name": "harshit",
                "email": "bhimaniharshi09904@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "flutter developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [],
                    "web": []
                }
            },
            {
                "name": "manthan15",
                "email": "bhavsarmanthan15@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "python developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token"
                    ],
                    "web": []
                }
            },
            {
                "name": "hemal",
                "email": "hemal@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "flutter developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token"
                    ],
                    "web": []
                }
            },
            {
                "name": "manthan5",
                "email": "manthan5@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "python developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token",
                        "device_token"
                    ],
                    "web": []
                }
            },
            {
                "name": "manthan3",
                "email": "manthan4@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "python developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [],
                    "web": []
                }
            },
            {
                "name": "manthan3",
                "email": "manthan3@gmail.com",
                "profile_url": "manthan1.jpg",
                "status": "online",
                "is_online": 'true',
                "deleted_record": 'false',
                "position": "python",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [
                        "device_token",
                        "device_token",
                        "device_token"
                    ],
                    "web": []
                }
            },
            {
                "name": "manthan2",
                "email": "manthan2@gmail.com",
                "profile_url": "manthan1.jpg",
                "status": "online",
                "is_online": 'true',
                "deleted_record": 'false',
                "position": "python",
                "deviceToken": {
                    "desktop": [
                        "token",
                        "token"
                    ],
                    "mobile": [
                        "token",
                        "token"
                    ],
                    "web": [
                        "token",
                        "token"
                    ]
                }
            }
        ]

data = {
                "name": "Hemal Moradiya",
                "email": "hemalmoradiya.ibl@gmail.com",
                "profile_url": "image_profile_url",
                "status": "available",
                "is_online": 'false',
                "deleted_record": 'false',
                "position": "flutter developer",
                "deviceToken": {
                    "desktop": [],
                    "mobile": [
                        "device_token",
                        "device_token"
                    ],
                    "web": []
                }
            }
# 3 

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import b64decode, b64encode

import json

backend = default_backend()




key = b64decode('heyFrj+egrMgWrt+hr//uhEFgbfEf/erFSEhbrphthw=')
iv = b64decode('YmRocm9xc3JlcG16ZGVoZQ==')


cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
padder = padding.PKCS7(128).padder()
# ďata = json.dumps(data)
ďata = 197475
data = str(ďata).encode('utf-8')
data = padder.update(data) + padder.finalize()
encryptor = cipher.encryptor()
c1 = encryptor.update(data) + encryptor.finalize()
ct_out = b64encode(c1)
print(ct_out)

# ct = 'UHG/Gb2IEZGWEBrgAg0NnDJnSSiSSq7HwIxX/raRPu9QW6Oh3XRfXoj0taQbWy3X'
# ct_out = b64decode(ct)

decryptor = cipher.decryptor()
unpadder = padding.PKCS7(128).unpadder()
plain = decryptor.update(c1) + decryptor.finalize()
plain = unpadder.update(plain) + unpadder.finalize()
plain = plain.decode("utf-8")
print(plain)





# from Crypto.Cipher import AES 
# import binascii,os
# import random, string

# # iv = os.urandom(16)
# iv = '5183666c72eec9e4'
# aes_mode = AES.MODE_CBC
# # key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
# key = 'bf3c199c2470cb477d907b1e0917c17b'
# print('key', key)

# encryptor = AES.new(key, aes_mode, iv)

# def aes_encrypt(plaintext):
#     plaintext = convert_to_16(plaintext)
#     print('plaintext', plaintext)

#     ciphertext = encryptor.encrypt(plaintext)
    
#     print(type(ciphertext))
#     return ciphertext

# def convert_to_16(plaintext): #Overcome the drawback of plaintxt size which should be multiple of len(iv)
#     add = 16 - (len(plaintext) % 16)
#     return(plaintext + ' ' * add)

# Encrypted = aes_encrypt('Hello world')

# print("Encrypted message :",Encrypted)

# aes = AES.new(key, AES.MODE_CBC, iv)
# decd = aes.decrypt(Encrypted)
# print(type(decd))
# print('decd', decd)

