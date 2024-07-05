import pandas as pd
from glob import glob

# Dapatkan daftar semua file CSV
csv_files = glob('datasets/branch_*.csv')

# Muat setiap file CSV ke dalam DataFrame dan simpan dalam sebuah list
dataframes = [pd.read_csv(file) for file in csv_files]

# Gabungkan semua DataFrame menjadi satu
combined_df = pd.concat(dataframes, ignore_index=True)

# Hapus baris dengan nilai NaN pada kolom 'transaction_id', 'date', dan 'customer_id'
cleaned_df = combined_df.dropna(subset=['transaction_id', 'date', 'customer_id'])

# Ubah kolom 'date' menjadi tipe datetime menggunakan .loc untuk menghindari peringatan
cleaned_df.loc[:, 'date'] = pd.to_datetime(cleaned_df['date'])

# Hapus duplikat berdasarkan 'transaction_id' dengan mempertahankan yang terbaru
cleaned_df = cleaned_df.sort_values('date').drop_duplicates(subset=['transaction_id'], keep='last')

# Hitung total penjualan per cabang
cleaned_df['total_sales'] = cleaned_df['quantity'] * cleaned_df['price']
total_sales_per_branch = cleaned_df.groupby('branch')['total_sales'].sum().reset_index()

# Simpan hasilnya ke file CSV baru
total_sales_per_branch.to_csv('total_sales_per_branch.csv', index=False)

print("Data manipulation and aggregation completed. Results saved to total_sales_per_branch.csv.")
