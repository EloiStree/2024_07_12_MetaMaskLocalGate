from web3 import Web3
from eth_account.messages import defunct_hash_message
message = "J'aime les frites !"
address = "0x75960Ef0B3325cCad2654FEf7eF096A9ED9A3FB8"
signed_message = "0xc0ee7896dba782f43fabfc011dff9bb677d712128523f4820f95ef20b86e0e583167e6cda8652f34f712fdcc4977eb024a49828930550590f27bdd4a766772ea1c"


from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct
w3 = Web3(Web3.HTTPProvider(""))
mesage= encode_defunct(text=message)
address_recovered = w3.eth.account.recover_message(mesage,signature=HexBytes(signed_message))
print(address_recovered+"\n+"+address)
if address ==address_recovered:
    print("Verified")
else:
    print("Not Verified")