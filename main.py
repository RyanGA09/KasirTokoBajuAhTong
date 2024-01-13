import uuid

from cassandra.cluster import Cluster
from cassandra.query import dict_factory

from create_produk_baju import create_produk_baju
from read_produk_baju import read_produk_baju
from update_produk_baju import update_produk_baju
from delete_produk_baju import delete_produk_baju

# Buat koneksi ke cluster
cluster = Cluster(['172.17.0.2'])
session = cluster.connect('toko_baju')

session.row_factory = dict_factory

# Contoh Penggunaan
create_produk_baju("Kemeja Putih", "Kemeja", "XL", 49.99, 100)
create_produk_baju("Celana Jeans", "Celana", "32", 59.99, 50)

produk_list = read_produk_baju()
print("Data Produk Baju:")
print(produk_list)

produk_id_to_update = produk_list[0]['id']
update_produk_baju(produk_id_to_update, 54.99, 80)

produk_list_after_update = read_produk_baju()
print("Data Produk Baju setelah Update:")
print(produk_list_after_update)

produk_id_to_delete = produk_list_after_update[1]['id']
delete_produk_baju(produk_id_to_delete)

produk_list_after_delete = read_produk_baju()
print("Data Produk Baju setelah Delete:")
print(produk_list_after_delete)

# Tutup koneksi
cluster.shutdown()