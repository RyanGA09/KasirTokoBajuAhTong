from cassandra.cluster import Cluster
from cassandra.query import dict_factory

def update_produk_baju(produk_id, harga_baru, stok_baru):
    cluster = Cluster(['172.17.0.2'])
    session = cluster.connect('toko_baju')

    session.row_factory = dict_factory

    query = "UPDATE produk_baju SET harga = %s, stok = %s WHERE id = %s"
    session.execute(query, (harga_baru, stok_baru, produk_id))

    # Tutup koneksi
    cluster.shutdown()