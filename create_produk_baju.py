import uuid

from cassandra.cluster import Cluster
from cassandra.query import dict_factory

def create_produk_baju(nama_produk, jenis_baju, ukuran, harga, stok):
    cluster = Cluster(['172.17.0.2'])
    session = cluster.connect('toko_baju')

    session.row_factory = dict_factory

    produk_id = uuid.uuid4()
    query = """
    INSERT INTO produk_baju (id, nama_produk, jenis_baju, ukuran, harga, stok)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    session.execute(query, (produk_id, nama_produk, jenis_baju, ukuran, harga, stok))

    # Tutup koneksi
    cluster.shutdown()