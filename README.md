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


```
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


