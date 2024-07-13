using System;
using System.Net.Sockets;
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


        Thread t = new Thread(new ThreadStart(VerifySignedMessageLoop));
        t.Start();

        Console.WriteLine("Press any key to exit...");
        

    }

    private static void VerifySignedMessageLoop()
    {
        UdpClient udpClient = new UdpClient(11000);
        while (true)
        {
            
        }
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
