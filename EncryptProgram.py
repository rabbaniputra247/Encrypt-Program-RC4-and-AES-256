import base64
import hashlib
from Crypto.Cipher import ARC4, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# FUNGSI BANTUAN
def hash_key(key):
    return hashlib.sha256(key.encode()).digest()

def input_data(is_decrypt=False):
    pilihan = input("Input (1) Teks atau (2) File ? ")

    if pilihan == "1":
        teks = input("Masukkan teks: ")
        if is_decrypt:
            return "teks", base64.b64decode(teks)
        else:
            return "teks", teks.encode()

    elif pilihan == "2":
        path = input("Masukkan nama file: ")
        with open(path, "rb") as f:
            return "file", f.read(), path

    else:
        print("Pilihan tidak valid")
        return None, None

# RC4
def rc4_encrypt(data, key):
    cipher = ARC4.new(key.encode())
    return cipher.encrypt(data)

def rc4_decrypt(data, key):
    cipher = ARC4.new(key.encode())
    return cipher.decrypt(data)

# AES-256
def aes_encrypt(data, key, mode):
    key = hash_key(key)

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(pad(data, 16))

    elif mode == "CBC":
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(pad(data, 16))

    elif mode == "CTR":
        cipher = AES.new(key, AES.MODE_CTR)
        return cipher.nonce + cipher.encrypt(data)

def aes_decrypt(data, key, mode):
    key = hash_key(key)

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        return unpad(cipher.decrypt(data), 16)

    elif mode == "CBC":
        iv = data[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(data[16:]), 16)

    elif mode == "CTR":
        nonce = data[:8]
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        return cipher.decrypt(data[8:])

# MENU
def tampilkan_menu():
    print("\nMENU")
    print("1. Enkripsi")
    print("   1.1 RC4")
    print("   1.2 AES")
    print("       1.2.1 Mode ECB")
    print("       1.2.2 Mode CBC")
    print("       1.2.3 Mode Counter")
    print("2. Dekripsi")
    print("   2.1 RC4")
    print("   2.2 AES")
    print("       2.2.1 Mode ECB")
    print("       2.2.2 Mode CBC")
    print("       2.2.3 Mode Counter")
    print("3. Keluar")

# PROGRAM UTAMA
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "3":
            print("Program selesai.")
            break

        key = input("Masukkan kunci: ")

        decrypt_mode = pilihan.startswith("2")
        tipe, data, *path = input_data(is_decrypt=decrypt_mode)
        if data is None:
            continue

        # ENKRIPSI
        if pilihan == "1.1":
            hasil = rc4_encrypt(data, key)

        elif pilihan == "1.2.1":
            hasil = aes_encrypt(data, key, "ECB")

        elif pilihan == "1.2.2":
            hasil = aes_encrypt(data, key, "CBC")

        elif pilihan == "1.2.3":
            hasil = aes_encrypt(data, key, "CTR")

        # DEKRIPSI
        elif pilihan == "2.1":
            hasil = rc4_decrypt(data, key)

        elif pilihan == "2.2.1":
            hasil = aes_decrypt(data, key, "ECB")

        elif pilihan == "2.2.2":
            hasil = aes_decrypt(data, key, "CBC")

        elif pilihan == "2.2.3":
            hasil = aes_decrypt(data, key, "CTR")

        else:
            print("Pilihan tidak valid")
            continue

        # OUTPUT
        if tipe == "teks":
            if pilihan.startswith("1"):
                print("Cipherteks (Base64):")
                print(base64.b64encode(hasil).decode())
            else:
                print("Hasil dekripsi:")
                print(hasil.decode())
        else:
            out = input("Nama file output: ")
            with open(out, "wb") as f:
                f.write(hasil)
            print("File berhasil disimpan.")

if __name__ == "__main__":
    main()