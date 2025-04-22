# 🕷️ Merayap

**Merayap** adalah tool sederhana berbasis Python untuk melakukan **crawling hasil pencarian Google** menggunakan keyword dan site tertentu. Cocok untuk riset, pengumpulan data, dan pemantauan informasi publik dari web.

---

## ✨ Fitur Utama

- Crawling hasil pencarian Google
- Filter berdasarkan keyword dan site
- Menyimpan hasil dalam format `.csv`
- Format CSV dipisahkan dengan `|` untuk kemudahan analisis data

---

## 📦 Setup Awal

1. Buat folder baru untuk proyek ini
2. Ekstrak isi `merayap.zip` ke dalam folder tersebut

---

## 🧪 Setup Lingkungan (Sekali Saja)

1. **Download Python (disarankan 3.13)**  
   🔗 [Unduh Python 3.13.1](https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe)

2. Klik kanan pada folder proyek, lalu pilih **Open in Terminal**

3. Jalankan perintah berikut untuk membuat virtual environment:
   ```bash
   python -m venv env
   
4. Aktifkan virtual environment:
   ```bash
   env\Scripts\activate

5. Install semua dependensi:
   ```bash
   pip install -r requirements.txt

6. Jalankan program:
   ```bash
   python rayap.py
