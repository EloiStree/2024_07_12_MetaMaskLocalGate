// ==UserScript==
// @name         Connect to MetaMask and Sign Message
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Connect to MetaMask, prompt for a message, and sign it using window.ethereum and web3.min.js
// @author       You
// @match        https://scratch.mit.edu/projects/editor/?tutorial=getStarted
// @grant        none
// @require      https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js
// ==/UserScript==

(async function() {
    'use strict';

    // Wait until window.ethereum is injected by MetaMask
    while (typeof window.ethereum === 'undefined') {
        await new Promise(resolve => setTimeout(resolve, 100));
    }

    // Request account access if needed
    try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
    } catch (error) {
        console.error('User denied account access:', error);
        return;
    }

    // Initialize web3
    const web3 = new Web3(window.ethereum);

    // Check if MetaMask is connected
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
        console.log('MetaMask is not connected');
        return;
    } else {
        console.log('MetaMask is connected. Account:', accounts[0]);
    }

    // Prompt user for a message to sign
    const message = prompt("Enter the message you want to sign:");

    if (message) {
        // Sign the message
        web3.eth.personal.sign(web3.utils.utf8ToHex(message), accounts[0], '')
            .then(signature => {
                console.log('Message signed:', signature);
                alert('Message signed successfully. Signature: ' + signature);
            })
            .catch(error => {
                console.error('Error signing message:', error);
                alert('Error signing message: ' + error.message);
            });
    } else {
        console.log('No message entered');
    }

})();
