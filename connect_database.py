from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider, SaslAuthProvider

cloud_config= {
        'secure_connect_bundle': 'D:/laptop/company/IBL infotech/topics/cassandra/secure-connect-cassandra-demo.zip'
}
CLIENT_ID = 'PspeojYBXydShOYEaYOyDFwu'
CLIENT_SECRET = 'R+0g0aAQrLu03gLkvZUxHBe.ZJSdxs_tlGzoB_L2XxikWj5gC7gj9YfH9,OlTc_ldpc2bCZh_CbdfmZcM-Ctq2CQRirWMH3OYnN,A0LjtDyYMyK,l0ZCFuHjsZIv8b0l'
auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# row = session.execute("select release_version from system.local").one()
# if row:
#     print(row[0])
# else:
#     print("An error occurred.")

demo = session.execute("CREATE KEYSPACE demo WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")
# keyspaces = session.execute("DESCRIBE python_demo")
print('demo', demo)