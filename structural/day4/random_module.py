"""  
writing a script that simulates a "Random Sampling" of data.

Import the random module.

Create a list of server IDs: servers = [101, 102, 103, 104, 105].

Use random.choice(list_name) to pick one random server from the list.

Print: "Connecting to random server: [ID]".

"""


import random

servers = [101,102,103,104,105]

ID = random.choice(servers)

print(f"Connecting to random server: {ID}")