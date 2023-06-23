#cal/callusion = m % k
#collusion / linear probbing

hash_table = [None] * 10

def hashFunction(value):
    return value % len(hash_table)

def insert(hash_table, value):
    hash_key = hashFunction(value)
    index = hash_key

    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)

    hash_table[index] = value

def search(value):
    hash_key = hashFunction(value)
    index = hash_key

    while hash_table[index] is not None:
        if hash_table[index] == value:
            return index
        index = (index + 1) % len(hash_table)
        return None

insert(hash_table, 5)
insert(hash_table, 17)
insert(hash_table, 13)
insert(hash_table, 21)
insert(hash_table, 15)
print(hash_table) 
print("index ke-", end="")
print(search(5))