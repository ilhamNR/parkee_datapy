# Data Manipulation App menggunakan Python dan Pandas

Aplikasi ini melakukan manipulasi data menggunakan Python dan Pandas untuk menggabungkan beberapa file CSV transaksi dari cabang-cabang toko, membersihkan data, dan menghitung total penjualan per cabang.

## Struktur Proyek

├── app.py
├── datasets
│ ├── branch_a.csv
│ ├── branch_b.csv
│ └── branch_c.csv
└─ requirements.txt



- **`app.py`**: File utama yang berisi skrip untuk menjalankan aplikasi.
- **`datasets/`**: Direktori yang berisi file-file CSV yang berisi data transaksi dari cabang-cabang toko.
- **`requirements.txt`**: Berkas yang berisi daftar pustaka Python yang diperlukan untuk menjalankan aplikasi.
- **`total_sales_per_branch.csv`**: Output dari aplikasi berupa file CSV yang berisi total penjualan per cabang setelah proses manipulasi data.

## Instalasi

1. Pastikan Anda memiliki Python yang terinstal di komputer Anda. Anda bisa mengunduhnya dari [python.org](https://www.python.org/).
2. Clone repositori ini ke direktori lokal Anda:

   ``` bash
   git clone https://github.com/ilhamnr/parkee_datapy.git
   cd nama-repositori 
3. Instal pustaka yang diperlukan menggunakan pip, dengan menjalankan perintah berikut:

bash
Copy code
pip install -r requirements.txt
## Penggunaan
Pastikan file CSV transaksi dari cabang-cabang toko sudah berada di dalam direktori datasets/.
Jalankan skrip Python app.py untuk menjalankan aplikasi:
python app.py

Skrip ini akan menggabungkan semua file CSV, membersihkan data, menghitung total penjualan per cabang, dan menyimpan hasilnya dalam file total_sales_per_branch.csv.

Setelah proses selesai, Anda dapat mengeksplor hasilnya dalam file total_sales_per_branch.csv.