from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'], control_connection_timeout=10,  port=9042)
cluster.connect()

# from cassandra.cluster import Cluster
# from cassandra.policies import DCAwareRoundRobinPolicy
# from cassandra.auth import PlainTextAuthProvider

# def cassandra_conn():

#    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
#    cluster = Cluster(['127.0.0.1'], load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='US-WEST'), port=9042, auth_provider=auth_provider)

#    session = cluster.connect()

#    return session, cluster

# cassandra_conn = cassandra_conn()
# print('cassandra_conn', cassandra_conn)