from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider, SaslAuthProvider

cloud_config= {
        'secure_connect_bundle': 'D:/laptop/company/IBL infotech/topics/cassandra/secure-connect-cassandra-demo.zip'
}

# CLIENT_ID = 'PspeojYBXydShOYEaYOyDFwu'
# CLIENT_SECRET = 'R+0g0aAQrLu03gLkvZUxHBe.ZJSdxs_tlGzoB_L2XxikWj5gC7gj9YfH9,OlTc_ldpc2bCZh_CbdfmZcM-Ctq2CQRirWMH3OYnN,A0LjtDyYMyK,l0ZCFuHjsZIv8b0l'

CLIENT_ID = 'grZJKnokKoUFnAbOsPACPAgv'
CLIENT_SECRET = ',yeH1xfOruZl2N9r1DGeMA8k5iyjE5Zz9NxqPM6QxcIfvd7UcQA7ha0JwTTYMaGEGxdX55xN3SY+uZwiLsaMSpOZeeOQ7DBxUejq7EYjIKA4h-Lc9MNIHPIoKvgN+NZ3'


auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")


# demo = session.execute("CREATE KEYSPACE demo WITH replication = {'class': 'NetworkTopologyStrategy', 'ap-southeast-1': '3'}  AND durable_writes = true")
demo = session.execute("CREATE KEYSPACE demo WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")
print('demo', demo)
# keyspaces = session.execute("DESCRIBE python_demo")
# print('keyspaces', keyspaces)





# from astrapy.rest import create_client, http_methods
# import uuid

# # get Astra connection information from environment variables
# ASTRA_DB_ID= '0e14d33e-6547-44d2-8089-3ccf94c4faaf'
# ASTRA_DB_REGION= 'ap-southeast-1'
# ASTRA_DB_APPLICATION_TOKEN= "AstraCS:grZJKnokKoUFnAbOsPACPAgv:946c78e3635304f5edd79d14dc80e08bf474d5222ed2de8ca7f81b342f07e054"
# ASTRA_DB_KEYSPACE = 'python_demo'
# ASTRA_DB_COLLECTION = "test"

# # setup an Astra Client
# astra_http_client = create_client(astra_database_id=ASTRA_DB_ID,
#                          astra_database_region=ASTRA_DB_REGION,
#                          astra_application_token=ASTRA_DB_APPLICATION_TOKEN)

# create a document on Astra using the Document API
# doc_uuid = uuid.uuid4()
# astra_http_client.request(
#     method=http_methods.PUT,
#     path=f"/api/rest/v2/namespaces/{ASTRA_DB_KEYSPACE}/collections/{ASTRA_DB_COLLECTION}/{doc_uuid}",
#     json_data={
#         "first_name": "Cliff",
#         "last_name": "Wicklow",
#         "emails": ["cliff.wicklow@example.com"],
#     })