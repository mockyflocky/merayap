🕷️ Merayap
Merayap adalah sebuah tool sederhana berbasis Python untuk melakukan crawling hasil pencarian Google menggunakan keyword dan site tertentu. Tool ini sangat cocok untuk keperluan riset data, monitoring brand, atau pengumpulan informasi publik secara cepat dan efisien.

✨ Fitur Utama
Crawling hasil pencarian Google

Dukungan keyword dan filter berdasarkan site/domain

Output hasil berupa file CSV

Format CSV menggunakan pemisah | untuk memudahkan pengolahan data lanjutan

🚀 Cara Menggunakan
🔧 Setup Awal
Buat folder baru untuk proyek ini

Ekstrak file merayap.zip ke dalam folder tersebut

📦 Setup Lingkungan (hanya sekali di awal)
Download Python (disarankan versi 3.13)
Unduh Python 3.13.1 di sini

Klik kanan pada folder proyek, lalu pilih "Open in Terminal"

Jalankan perintah untuk membuat virtual environment:

bash
Copy
Edit
python -m venv env
Aktifkan lingkungan virtual:

Di Windows:

bash
Copy
Edit
env\Scripts\activate
Setelah aktif, akan muncul tanda (env) di awal terminal

Install semua kebutuhan:

bash
Copy
Edit
pip install -r requirements.txt
Jalankan program:

bash
Copy
Edit
python rayap.py
🔁 Setup Harian (untuk penggunaan selanjutnya)
Klik kanan pada folder proyek, buka terminal

Aktifkan lingkungan virtual:

bash
Copy
Edit
env\Scripts\activate
Jalankan program:

bash
Copy
Edit
python rayap.py
📂 Output
Hasil crawling akan disimpan dalam file CSV dengan format:

nginx
Copy
Edit
Judul | Cuplikan | Link
Data ini bisa kamu olah lagi menggunakan Excel, Google Sheets, atau script Python tambahan.

💬 Catatan Tambahan
Gunakan keyword dan site dengan bijak, sesuai kebutuhan

Hindari crawling dalam volume besar dalam waktu singkat agar tidak dianggap bot oleh Google

Jika mengalami kendala, pastikan koneksi internet stabil dan periksa kembali keyword yang digunakan

📫 Kontribusi & Kontak
Project ini masih dalam tahap pengembangan. Jika ingin berkontribusi atau ada pertanyaan, silakan buat issue atau pull request.

