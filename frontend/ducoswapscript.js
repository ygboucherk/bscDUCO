// 3 gwei or 3 billions wei
const GAS_PRICE = 3000000000;
const GAS_LIMIT = 300000;	// 300000 gas units

async function refreshBalances() {
    document.getElementById("balancelabel").innerHTML = (Math.floor(Number(await duco.methods.balanceOf(currentAddress).call()) / 10 ** 8) / 10 ** 10);
}

async function userExists(user) {
    return ((await (await fetch(`https://server.duinocoin.com/users/${user}`)).json()).success);
}

abi = [{
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "owner",
        "type": "address"
    }, {
        "indexed": true,
        "internalType": "address",
        "name": "spender",
        "type": "address"
    }, {
        "indexed": false,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
    }],
    "name": "Approval",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }],
    "name": "RevokeWrapper",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
    }, {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
    }, {
        "indexed": false,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
    }],
    "name": "Transfer",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }, {
        "indexed": false,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
    }, {
        "indexed": true,
        "internalType": "string",
        "name": "_ducoUsername",
        "type": "string"
    }],
    "name": "UnwrapConfirmed",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }, {
        "indexed": false,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
    }, {
        "indexed": true,
        "internalType": "string",
        "name": "_ducoUsername",
        "type": "string"
    }],
    "name": "UnwrapInitiated",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }, {
        "indexed": false,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
    }],
    "name": "Wrap",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }],
    "name": "allowWrapper",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "_oldAdmin",
        "type": "address"
    }, {
        "indexed": true,
        "internalType": "address",
        "name": "_newAdmin",
        "type": "address"
    }],
    "name": "changeAdminConfirmed",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{
        "indexed": true,
        "internalType": "address",
        "name": "_currentAdmin",
        "type": "address"
    }, {
        "indexed": true,
        "internalType": "address",
        "name": "_newAdmin",
        "type": "address"
    }],
    "name": "changeAdminRequest",
    "type": "event"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }],
    "name": "ChangeAdmin",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }],
    "name": "addWrapperAccess",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "owner",
        "type": "address"
    }, {
        "internalType": "address",
        "name": "spender",
        "type": "address"
    }],
    "name": "allowance",
    "outputs": [{
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "spender",
        "type": "address"
    }, {
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
    }],
    "name": "approve",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "account",
        "type": "address"
    }],
    "name": "balanceOf",
    "outputs": [{
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [],
    "name": "cancelChangeAdmin",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }, {
        "internalType": "string",
        "name": "_ducousername",
        "type": "string"
    }],
    "name": "cancelWithdrawals",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }],
    "name": "checkWrapperStatus",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [],
    "name": "confirmChangeAdmin",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "string",
        "name": "_ducousername",
        "type": "string"
    }, {
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }, {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
    }],
    "name": "confirmWithdraw",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [],
    "name": "currentAdmin",
    "outputs": [{
        "internalType": "address",
        "name": "",
        "type": "address"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [],
    "name": "decimals",
    "outputs": [{
        "internalType": "uint8",
        "name": "",
        "type": "uint8"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "spender",
        "type": "address"
    }, {
        "internalType": "uint256",
        "name": "subtractedValue",
        "type": "uint256"
    }],
    "name": "decreaseAllowance",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [],
    "name": "getUserList",
    "outputs": [{
        "components": [{
            "internalType": "address",
            "name": "_address",
            "type": "address"
        }, {
            "internalType": "string",
            "name": "username",
            "type": "string"
        }, {
            "internalType": "uint256",
            "name": "pendingBalance",
            "type": "uint256"
        }],
        "internalType": "struct ERC20.addressUsername[]",
        "name": "",
        "type": "tuple[]"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "spender",
        "type": "address"
    }, {
        "internalType": "uint256",
        "name": "addedValue",
        "type": "uint256"
    }],
    "name": "increaseAllowance",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "string",
        "name": "_ducousername",
        "type": "string"
    }, {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
    }],
    "name": "initiateWithdraw",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [],
    "name": "name",
    "outputs": [{
        "internalType": "string",
        "name": "",
        "type": "string"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }, {
        "internalType": "string",
        "name": "_ducousername",
        "type": "string"
    }],
    "name": "pendingWithdrawals",
    "outputs": [{
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "bytes",
        "name": "",
        "type": "bytes"
    }],
    "name": "positionInList",
    "outputs": [{
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }],
    "name": "revokeWrapperAccess",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [],
    "name": "symbol",
    "outputs": [{
        "internalType": "string",
        "name": "",
        "type": "string"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [],
    "name": "totalSupply",
    "outputs": [{
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "recipient",
        "type": "address"
    }, {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
    }],
    "name": "transfer",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "sender",
        "type": "address"
    }, {
        "internalType": "address",
        "name": "recipient",
        "type": "address"
    }, {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
    }],
    "name": "transferFrom",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "bytes",
        "name": "",
        "type": "bytes"
    }],
    "name": "userExists",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
    }],
    "name": "usersList",
    "outputs": [{
        "internalType": "address",
        "name": "_address",
        "type": "address"
    }, {
        "internalType": "string",
        "name": "username",
        "type": "string"
    }, {
        "internalType": "uint256",
        "name": "pendingBalance",
        "type": "uint256"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [],
    "name": "usersListLength",
    "outputs": [{
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
    }],
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [{
        "internalType": "address",
        "name": "_tronaddress",
        "type": "address"
    }, {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
    }],
    "name": "wrap",
    "outputs": [{
        "internalType": "bool",
        "name": "",
        "type": "bool"
    }],
    "stateMutability": "nonpayable",
    "type": "function"
}]
contract = "";
ticker = null;

function setSymbol(_symbol) {
    document.getElementById("tokenpageload").innerHTML = _symbol;
    document.getElementById("tokenInInput").innerHTML = _symbol;
    document.getElementById("tokenInTitle").innerHTML = _symbol;
    document.getElementById("tokenInTitle2").innerHTML = _symbol;
    ticker = _symbol;
}

// Connect using a discovered EIP-1193 provider.
// (Modern MetaMask v12+ no longer auto-injects window.ethereum;
//  it announces providers via EIP-6963 events instead.)
function connectWallet(provider) {
    window.ethereum = provider;
    window.web3 = new Web3(provider);
    return provider.request({ method: 'eth_requestAccounts' }).then(async function(accounts) {
        currentAddress = accounts[0];
        const chainId = await web3.eth.getChainId();
        if (chainId == 56) {
            console.log("Correctly connected to BSC");
            setSymbol("bscDUCO");
            window.correctRpc = true;
            duco = new web3.eth.Contract(abi,"0xCF572cA0AB84d8Ce1652b175e930292E2320785b");
            refreshBalances();
        } else if (chainId == 137) {
            console.log("Correctly connected to Polygon");
            setSymbol("maticDUCO");
            window.correctRpc = true;
            duco = new web3.eth.Contract(abi,"0xaf965beB8C830aE5dc8280d1c7215B8F0aCC0CeA");
            refreshBalances();
        } else if (chainId == 42220) {
            console.log("Correctly connected to Celo");
            setSymbol("celoDUCO");
            window.correctRpc = true;
            duco = new web3.eth.Contract(abi,"0xDB452CC669D3Ae454226AbF232Fe211bAfF2a1F9");
            refreshBalances();
        } else if (chainId == 1380996178) {
            console.log("Correctly connected to RaptorChain");
            setSymbol("rDUCO");
            window.correctRpc = true;
            duco = new web3.eth.Contract(abi,"0x9ffE5c6EB6A8BFFF1a9a9DC07406629616c19d32");
            refreshBalances();
        } else {
            alert("Error, current chainId is " + chainId + ", please switch to BSC/MATIC/CELO and refresh this page");
            window.correctRpc = false;
        }
    }).catch(function(err) {
        // MetaMask can reject the connect request with its generic
        // "Unexpected error" (its own selectExtension step failed). Don't let
        // that surface as an unhandled rejection; report it and reset state so
        // the user can retry.
        console.error("eth_requestAccounts failed:", err && err.message ? err.message : err);
        window.correctRpc = false;
        window.metamaskInstalled = false;
        try {
            document.getElementById("networklabel").innerHTML =
                "Network : connection to wallet failed \u2014 please refresh and try again";
        } catch (ignored) {}
    });
}

function noWalletFound() {
    window.metamaskInstalled = false;
    // The #networklabel element may not exist on every page - guard it so the
    // install alert below always runs even when the element is missing.
    try {
        document.getElementById("networklabel").innerHTML = "Network : Please install a web3 compatible wallet";
    } catch (ignored) {}
    alert("No Web3-compatible wallet installed, please consider installing one !")
}

function detectWallet() {
    // Discovery strategy (per MetaMask docs & EIP-6963):
    //
    // * EIP-6963 is the PRIMARY mechanism - MetaMask explicitly recommends it
    //   over window.ethereum. Wallets announce themselves with a stable
    //   reverse-DNS id `info.rdns` (MetaMask == 'io.metamask',
    //   Phantom == 'app.phantom', Coinbase == 'com.coinbase.wallet', ...).
    // * Because Phantom (and others) also inject window.ethereum, grabbing that
    //   injected provider synchronously on load can pick the WRONG wallet and
    //   race MetaMask's own extension-selection (the "Unexpected error"). So we
    //   let EIP-6963 announce first, prefer MetaMask by rdns, and only fall
    //   back to the injected provider if nothing (better) was found.
    //
    // Note: we deliberately do NOT identify MetaMask via `isMetaMask` or its
    // display name - MetaMask's own docs flag `isMetaMask` as non-standard and
    // say other wallets may also set it true. `rdns` is the stable id to select on.

    var providers = [];
    var connected = false;

    function providerKey(detail) {
        if (!detail || !detail.info) return null;
        return detail.info.rdns || detail.info.uuid || detail.info.name;
    }

    function isMetaMask(p) {
        return p && p.info && p.info.rdns &&
               p.info.rdns.toLowerCase() === 'io.metamask';
    }

    function announceProvider(detail) {
        if (!detail || !detail.provider) return;
        // De-duplicate. Some wallets announce more than once (and can reappear
        // under a fresh uuid per session), which is what makes MetaMask's own
        // selectExtension step race. Stable key is rdns, then uuid, then name.
        var key = providerKey(detail);
        if (key && providers.some(function(p) { return providerKey(p) === key; })) return;
        providers.push(detail);
        tryConnect();
    }

    function tryConnect() {
        if (connected) return;
        // If MetaMask is announced, connect to it immediately. Otherwise HOLD:
        // do NOT bind to whichever wallet happens to announce first (Phantom can
        // beat MetaMask in announcement order). We settle after the announce
        // window in the timeout below, so MetaMask always wins when present.
        var mm = providers.find(isMetaMask);
        if (mm) {
            connected = true;
            window.metamaskInstalled = true;
            connectWallet(mm.provider);
        }
    }

    window.addEventListener('eip6963:announceProvider', function(e) {
        announceProvider(e.detail);
    });
    // Ask wallets to announce themselves.
    window.dispatchEvent(new Event('eip6963:requestProvider'));

    // After the announce window, settle on the best wallet: MetaMask if present,
    // otherwise the first announced wallet, otherwise the legacy injected
    // provider (covers older wallets that don't implement EIP-6963 yet).
    setTimeout(function() {
        if (connected) return;
        var chosen = providers.find(isMetaMask) || providers[0];
        if (chosen) {
            connected = true;
            window.metamaskInstalled = true;
            connectWallet(chosen.provider);
            return;
        }
        if (window.ethereum && window.ethereum.request) {
            connected = true;
            window.metamaskInstalled = true;
            connectWallet(window.ethereum);
        }
    }, 600);

    // Nothing found at all -> install prompt.
    setTimeout(function() {
        if (!connected) {
            noWalletFound();
        }
    }, 2500);
}

detectWallet();

async function unwrapDUCO() {
    amount = document.getElementById("amountInput").value
    amount = web3.utils.toWei(amount, "ether")
    username = document.getElementById("usernameInput").value
	
	if (username == "" || !(await userExists(username))) {
        alert("Invalid username specified");
		return;
	}
	
	// wei amount
	let _currentWbalance = BigInt(await duco.methods.balanceOf(currentAddress).call());
	if (_currentWbalance < BigInt(amount)) {
		alert("Insufficient balance");
		return;
	}
    _call = duco.methods.initiateWithdraw(username, BigInt(amount));
    console.log(_call);
    
	await _call.send({
		'from': currentAddress,
		'gasPrice': GAS_PRICE,
		'gas': GAS_LIMIT,
        'type': 0
	});
	await refreshBalances();
}

async function addtomask() {
    if (window.correctRpc) {
        await ethereum.request({
            method: 'wallet_watchAsset',
            params: {
                type: 'ERC20',
                options: {
                    address: duco._address,
                    symbol: ticker,
                    decimals: 18,
                    image: "https://bsc.duinocoin.com/ducowhite.png",
                },
            },
        });
    }
}

