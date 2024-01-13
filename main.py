import uuid

from cassandra.cluster import Cluster
from cassandra.query import dict_factory

# Buat koneksi ke cluster
cluster = Cluster(['172.17.0.2'])
session = cluster.connect('toko_baju')

session.row_factory = dict_factory

def create_produk_baju(nama_produk, jenis_baju, ukuran, harga, stok):
    produk_id = uuid.uuid4()
    query = """
    INSERT INTO produk_baju (id, nama_produk, jenis_baju, ukuran, harga, stok)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    session.execute(query, (produk_id, nama_produk, jenis_baju, ukuran, harga, stok))

def read_produk_baju():
    query = "SELECT * FROM produk_baju"
    result = session.execute(query)
    return result.all()

def update_produk_baju(produk_id, harga_baru, stok_baru):
    query = "UPDATE produk_baju SET harga = %s, stok = %s WHERE id = %s"
    session.execute(query, (harga_baru, stok_baru, produk_id))

def delete_produk_baju(produk_id):
    query = "DELETE FROM produk_baju WHERE id = %s"
    session.execute(query, (produk_id,))

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
