"""
The Database Connector): Write a function that simulates connecting to a database.

Define connect_db.

It takes two arguments: host and port.

Set port to have a default value of 5432 (standard PostgreSQL port).

Inside, return a string: "Connected to {host} on port {port}".

Call it twice:

Once with host="localhost" (let it use the default port).

Once with host="prod-db" and port=3306.

Print both results.

"""


def connect_db(host, port=5432):
    return f"Connected to {host} on port {port}"

print(connect_db("localhost"))
print(connect_db("prod_db",3306))

