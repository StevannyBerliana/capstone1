# Sales and Marketing Data Management

## Overview
This Python script allows users to manage sales and marketing data by providing functionalities such as reading, adding, updating, deleting, filtering, and generating sales reports. The program uses the `tabulate` module for better data visualization.

## Features
- Display sales and marketing data in a tabular format
- Add new sales transactions with automatic transaction ID generation
- Update existing sales transaction details
- Delete transactions (with a recycle bin for data recovery)
- Restore deleted transactions from the recycle bin
- Filter transactions based on product name and marketing method
- Generate sales reports with highest/lowest sales, best-selling products, and most effective marketing methods

## Requirements
Ensure you have Python installed along with the required module:

```sh
pip install tabulate
```

## How to Use
Run the script using the command:

```sh
python script.py
```

### Menu Options
Once executed, the script provides the following menu:

1. **Tampilkan Data** – Displays all sales and marketing transactions.
2. **Tambah Data** – Adds a new transaction.
3. **Update Data** – Updates existing transactions.
4. **Hapus Data** – Moves a transaction to the recycle bin.
5. **Pulihkan Data** – Restores a deleted transaction from the recycle bin.
6. **Cari Data Berdasarkan Nama Barang dan Metode Pemasaran** – Filters transactions by product name or marketing method.
7. **Tampilkan Laporan Penjualan dan Pemasaran** – Generates a sales report.
8. **Keluar** – Exits the program.

## Data Structure
Each transaction contains the following details:
- `id_transaksi` (Generated automatically)
- `tanggal_transaksi` (Transaction date)
- `nama_barang` (Product name)
- `jumlah_penjualan` (Quantity sold)
- `harga` (Price per unit)
- `total_penjualan` (Total sales amount)
- `metode_pemasaran` (Marketing method used)
- `biaya_pemasaran` (Marketing cost)

## Example Output
### Displaying Data
```
+--------------+------------------+------------+----------------+----------+----------------+------------------+----------------+
| id_transaksi | tanggal_transaksi | nama_barang | jumlah_penjualan | harga    | total_penjualan | metode_pemasaran | biaya_pemasaran |
+--------------+------------------+------------+----------------+----------+----------------+------------------+----------------+
| TRX324       | 01-02-2024       | Laptop     | 10             | 7000000  | 70000000       | Ads Sosial Media | 500000         |
| TRX198       | 02-02-2024       | Smartphone | 15             | 5000000  | 75000000       | Email Marketing  | 300000         |
+--------------+------------------+------------+----------------+----------+----------------+------------------+----------------+
```

### Adding Data
```
Masukkan tanggal transaksi (DD-MM-YYYY): 15-02-2024
Masukkan Nama Barang: Laptop
Masukkan Jumlah Penjualan: 5
Masukkan Harga: 8000000
Masukkan Metode Pemasaran: Ads Sosial Media
Masukkan Biaya Pemasaran: 250000
Data Penjualan Berhasil Ditambahkan!
```

### Sales Report
```
=== Laporan Penjualan dan Pemasaran ===
+--------------------+--------------+------------+----------------+
| Kategori          | ID Transaksi | Nama Barang | Total Penjualan |
+--------------------+--------------+------------+----------------+
| Penjualan Tertinggi | TRX198       | Smartphone | 75000000       |
| Penjualan Terendah  | TRX324       | Laptop     | 70000000       |
+--------------------+--------------+------------+----------------+
```

## Contributions
Feel free to contribute by submitting pull requests or reporting issues.

## License
This project is open-source and available under the MIT License.
