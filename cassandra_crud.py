from cassandra.cluster import Cluster
import uuid

# Conectar ao Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect()

# Criar Keyspace e Tabela
session.execute("""
CREATE KEYSPACE IF NOT EXISTS mykeyspace
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")
session.execute("""
CREATE TABLE IF NOT EXISTS mykeyspace.users (
    id UUID PRIMARY KEY,
    name text,
    age int
)
""")

# Create
user_id = uuid.uuid4()
session.execute("""
INSERT INTO mykeyspace.users (id, name, age) VALUES (%s, %s, %s)
""", (user_id, 'John', 30))

# Read
rows = session.execute("""
SELECT * FROM mykeyspace.users WHERE id=%s
""", (user_id,))
for row in rows:
    print(f'Read from Cassandra: {row}')

# Update
session.execute("""
UPDATE mykeyspace.users SET age=%s WHERE id=%s
""", (31, user_id))

# Delete
session.execute("""
DELETE FROM mykeyspace.users WHERE id=%s
""", (user_id,))
