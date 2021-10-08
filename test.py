from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'], control_connection_timeout=10,  port=9042)
session = cluster.connect()
# print('session', session)

# session.execute("CREATE KEYSPACE demo WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")
# session.execute("CREATE TABLE demo.users (lastname text PRIMARY KEY, firstname text, email text)")
# session.execute("""
#     INSERT INTO demo.users
#     (lastname, firstname, email)
#      VALUES (%s,%s,%s)
#     """,
#     ("Brutus", "Marcus", "marcus@example.com")
# )
# session.execute("""
#     INSERT INTO demo.users
#     (lastname, firstname, email)
#      VALUES (%s,%s,%s)
#     """,
#     ("Caesar", "Julius", "caesar@example.com")
# )

# result = session.execute("""
#     SELECT * FROM demo.users WHERE lastname = %s
#     """,
#     ["Brutus"]).one()
# print('result', result)
# print(result.firstname, result.email)

# result = session.execute("""
#     SELECT * FROM demo.users WHERE lastname = %s
#     """,
#     ["Caesar"]).one()
# print(result.firstname, result.email)

# rows = session.execute('SELECT lastname, firstname, email FROM demo.users')
# for row in rows:
#     print('lastname', row.lastname, 'firstname', row.firstname, 'email', row.email)

# rows = session.execute('SELECT lastname, firstname, email FROM demo.users')
# for (lastname, firstname, email) in rows:
#     print(lastname, firstname, email)

rows = session.execute('SELECT lastname, firstname, email FROM demo.users')
for row in rows:
    print(row[0], row[1], row[2])


# session.execute("""
#     UPDATE demo.users SET email =%s WHERE lastname = %s
#     """,
#     ["mb@example.com", "Brutus"])

# session.execute("""
#     UPDATE demo.users SET email =%s WHERE lastname = %s
#     """,
#     ["jc@example.com", "Caesar"])

# result = session.execute("""
#     SELECT * FROM demo.users WHERE lastname = %s
#     """,
#     ["Caesar"]).one()
# print(result.firstname, result.email)

# session.execute("""
#     DELETE FROM demo.users WHERE lastname = %s
#     """,
#     ["Brutus"])