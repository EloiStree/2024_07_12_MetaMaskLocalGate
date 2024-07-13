# 2024_07_12_MetaMaskLocalGate
Just a local gate to MetaMask sign from local code 





Pure JS:
https://docs.metamask.io/wallet/how-to/use-sdk/javascript/pure-js/


Documentation:
- Plan https://docs.metamask.io/wallet/concepts/sdk/connections/ 

What is Meta Mask ?
- https://cryptoast.fr/tutoriel-metamask/


Based challenged:
[![image](https://github.com/user-attachments/assets/b1524759-0f3b-4acb-8f46-f57a6ebc91d1)](https://ethglobal.com/events/brussels/prizes#metamask-and-linea)
- https://youtu.be/Tx0V00Fs1Oo
- https://github.com/MetaMask/snaps/discussions/2471



That what I need but not in react https://codesandbox.io/s/react-eth-metamask-signatures-ibuxj?file=/public/index.html
-  What I need https://youtu.be/6BNcpjOebb0



Example: 
Message:J'aime les frites !
Address:0x75960Ef0B3325cCad2654FEf7eF096A9ED9A3FB8
Signed:0xc0ee7896dba782f43fabfc011dff9bb677d712128523f4820f95ef20b86e0e583167e6cda8652f34f712fdcc4977eb024a49828930550590f27bdd4a766772ea1c




Have signed message in WalletConenct: 
https://youtu.be/aCiBPDEasTE


# Server connection

Client code: Hello 0x75960Ef0B3325cCad2654FEf7eF096A9ED9A3FB8
Server code: SIGNIN:TEXT-GUID-LONG-TEXT
UI display: Sign "TEXT-GUID-LONG-TEXT" and past it back
User: Copy text and copy response
Client: SIGNED:0xc0ee7896dba782f43fabfc011dff9bb677d712128523f4820f95ef20b86e0e583167e6cda8652f34f712fdcc4977eb024a49828930550590f27bdd4a766772ea1c
Server: NetworkId:5 (close connection if not right)


 # Verified a user 
 ! Message must be random every time
``` csharp
using System;
using Nethereum.Signer;
using Nethereum.Util;

class Program
{
    static void Main()
    {
        string message = "J'aime les frites !";
        string address = "0x75960Ef0B3325cCad2654FEf7eF096A9ED9A3FB8";
        string signedMessage = "0xc0ee7896dba782f43fabfc011dff9bb677d712128523f4820f95ef20b86e0e583167e6cda8652f34f712fdcc4977eb024a49828930550590f27bdd4a766772ea1c";
        bool isValid = VerifySignedMessage(message, address, signedMessage);
        Console.WriteLine($"Is the signature valid? {isValid}");

    }

    public static bool VerifySignedMessage(string message, string address, string signedMessage)
    {
        var signer = new EthereumMessageSigner();
        var addressUtil = new AddressUtil();

        // Convert the address to its checksum format
        var checksumAddress = addressUtil.ConvertToChecksumAddress(address);

        // Recover the address from the signed message
        var recoveredAddress = signer.EncodeUTF8AndEcRecover(message, signedMessage);

        // Compare the recovered address with the provided address
        return string.Equals(checksumAddress, recoveredAddress, StringComparison.OrdinalIgnoreCase);
    }
}
```

``` python
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
```


---------------

# Alternative
- Wallet Connect: https://walletconnect.com
- Web3Auth: https://web3auth.io
- Privy: https://www.privy.io

