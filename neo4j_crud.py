from neo4j import GraphDatabase

# Connect to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "mypassword"
driver = GraphDatabase.driver(uri, auth=(username, password))

def create_person(tx, name, age):
    tx.run("CREATE (a:Person {name: $name, age: $age})", name=name, age=age)

def find_person(tx, name):
    result = tx.run("MATCH (a:Person {name: $name}) RETURN a.name AS name, a.age AS age", name=name)
    for record in result:
        print(f"Read from Neo4j: {record['name']}, {record['age']}")

def update_person(tx, name, age):
    tx.run("MATCH (a:Person {name: $name}) SET a.age = $age", name=name, age=age)

def delete_person(tx, name):
    tx.run("MATCH (a:Person {name: $name}) DELETE a", name=name)

with driver.session() as session:
    # Create
    session.write_transaction(create_person, "John", 30)
    # Read
    session.read_transaction(find_person, "John")
    # Update
    session.write_transaction(update_person, "John", 31)
    # Delete
    session.write_transaction(delete_person, "John")

# Close the connection
driver.close()

