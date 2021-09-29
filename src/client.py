import os
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

# Create the addresses

# Get the seed from environment variable
IOTA_SEED_SECRET = os.getenv('IOTA_SEED_SECRET')

if not IOTA_SEED_SECRET: 
    IOTA_SEED_SECRET="8d4fa37be3c00691131c2c3e03e7b8b956c9118a2ce4be3a8597d51d82ed2de9"   

client = iota_client.Client()

address_changed_list = client.get_addresses(    
                                            seed=IOTA_SEED_SECRET,    
                                            account_index=0,    
                                            input_range_begin=0,    
                                            input_range_end=10,    
                                            get_all=True)

print(address_changed_list) # Account starts with 'atoi' means testnet
