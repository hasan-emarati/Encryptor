from cryptography.fernet import Fernet

key = 'VlD8h2tEiJkQpKKnDNKnu8ya2fpIBMOo5oc7JKNasvk='
f = Fernet(key)

with open('G:\Git\Git_Hub\App\Encryptor\Tools\grades.txt', 'r') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_grades.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
