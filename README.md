PROGRAM ENKRIPSI DAN DEKRIPSI
RC4 DAN AES-256

Deskripsi:
Program ini merupakan aplikasi berbasis Python yang
mengimplementasikan algoritma kriptografi RC4 dan AES-256
(mode ECB, CBC, dan Counter). Program dapat digunakan untuk
mengenkripsi dan mendekripsi pesan berupa teks maupun file.

Kebutuhan Sistem:
- Python 3.x
- Library pycryptodome

Cara Instalasi:
1. Pastikan Python telah terpasang
2. Install library pycryptodome dengan perintah:
   pip install pycryptodome

Cara Menjalankan Program:
1. Buka terminal atau command prompt
2. Masuk ke folder program
3. Jalankan perintah:
   python EncryptProgram.py

Cara Penggunaan:
1. Pilih menu Enkripsi atau Dekripsi
2. Pilih algoritma RC4 atau AES-256
3. Jika AES, pilih mode ECB, CBC, atau Counter
4. Pilih input berupa teks atau file
5. Masukkan kunci
6. Program akan menampilkan hasil atau menyimpan file output

Catatan:
- Untuk teks, cipherteks ditampilkan dalam format Base64
- Untuk file, hasil disimpan dalam bentuk file biner
