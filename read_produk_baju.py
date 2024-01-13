from cassandra.cluster import Cluster
from cassandra.query import dict_factory

def read_produk_baju():
    cluster = Cluster(['172.17.0.2'])
    session = cluster.connect('toko_baju')

    session.row_factory = dict_factory

    query = "SELECT * FROM produk_baju"
    result = session.execute(query)
    data = result.all()

    # Tutup koneksi
    cluster.shutdown()

    return data