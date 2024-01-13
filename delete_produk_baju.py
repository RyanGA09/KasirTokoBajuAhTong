from cassandra.cluster import Cluster
from cassandra.query import dict_factory

def delete_produk_baju(produk_id):
    cluster = Cluster(['172.17.0.2'])
    session = cluster.connect('toko_baju')

    session.row_factory = dict_factory

    query = "DELETE FROM produk_baju WHERE id = %s"
    session.execute(query, (produk_id,))

    # Tutup koneksi
    cluster.shutdown()