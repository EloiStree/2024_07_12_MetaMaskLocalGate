import asyncio
import websockets
from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct

import asyncio
import websockets

async def handler(websocket, path):
    print(f"Client connected: {websocket.remote_address}")
    message = "J'aime les frites !"
    address = "0x75960Ef0B3325cCad2654FEf7eF096A9ED9A3FB8"
    signed_message = "0xc0ee7896dba782f43fabfc011dff9bb677d712128523f4820f95ef20b86e0e583167e6cda8652f34f712fdcc4977eb024a49828930550590f27bdd4a766772ea1c"
    #given_text = "J'aime les frites !|0x75960Ef0B3325cCad2654FEf7eF096A9ED9A3FB8|0xc0ee7896dba782f43fabfc011dff9bb677d712128523f4820f95ef20b86e0e583167e6cda8652f34f712fdcc4977eb024a49828930550590f27bdd4a766772ea1c"

    try:
        async for given_text in websocket:
            print(f"Received: {given_text}")
            tokens = given_text.split('|')
            bool_is_verified = False
            # Ensuring that the length of tokens is exactly 3
            if len(tokens) == 3:
                message, address, signed_message = tokens
                # Printing the variables to verify
                print("Message:", message)
                print("Address:", address)
                print("Signed Message:", signed_message)
                w3 = Web3(Web3.HTTPProvider(""))
                mesage= encode_defunct(text=message)
                address_recovered = w3.eth.account.recover_message(mesage,signature=HexBytes(signed_message))
                print(address_recovered+"\n+"+address)
                bool_is_verified = address ==address_recovered
        
            await websocket.send(message)
            string_respond =f"Fail|{response}"
            if bool_is_verified:
                string_respond= f"Verified|{response}"
            print(string_respond)
            await websocket.send(string_respond)
    except websockets.ConnectionClosed as e:
        print(f"Client disconnected: {websocket.remote_address} ({e.code} - {e.reason})")
    finally:
        await websocket.close()

async def main():
    async with websockets.serve(handler, "0.0.0.0", 6451):
        print("WebSocket server started on ws://0.0.0.0:6451")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
