import iota_client

print("Info:")
print(iota_client.__doc__)
print(dir(iota_client))

print("Connecting to testnet client")
# client will connect to testnet by default
client = iota_client.Client()

if client.get_health():
    print(client.get_info())
else:
    print("Testnet not healthy")