import requests, time, json, eth_account
global network, token, gasprice, _chainid, pendingBalances, pendingBalancesToken, abi, wrapperUsername, wrapperPassword, alreadyProcessed, config
from duco_api import Wallet
from web3 import Web3


gasprice = {}
network = {}
token = {}

_configLocation = "wrapperConfig.json"




abi = """[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"}],"name":"RevokeWrapper","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":true,"internalType":"string","name":"_ducoUsername","type":"string"}],"name":"UnwrapConfirmed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":true,"internalType":"string","name":"_ducoUsername","type":"string"}],"name":"UnwrapInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"Wrap","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"}],"name":"allowWrapper","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_oldAdmin","type":"address"},{"indexed":true,"internalType":"address","name":"_newAdmin","type":"address"}],"name":"changeAdminConfirmed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_currentAdmin","type":"address"},{"indexed":true,"internalType":"address","name":"_newAdmin","type":"address"}],"name":"changeAdminRequest","type":"event"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"ChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"addWrapperAccess","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cancelChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"_ducousername","type":"string"}],"name":"cancelWithdrawals","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"checkWrapperStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"confirmChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_ducousername","type":"string"},{"internalType":"address","name":"_address","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"confirmWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentAdmin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getUserList","outputs":[{"components":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"username","type":"string"},{"internalType":"uint256","name":"pendingBalance","type":"uint256"}],"internalType":"struct ERC20.addressUsername[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_ducousername","type":"string"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"initiateWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"_ducousername","type":"string"}],"name":"pendingWithdrawals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"","type":"bytes"}],"name":"positionInList","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"revokeWrapperAccess","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"","type":"bytes"}],"name":"userExists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"usersList","outputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"username","type":"string"},{"internalType":"uint256","name":"pendingBalance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"usersListLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tronaddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"wrap","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]"""

alreadyProcessed = []
pendingBalances = {} # good old mappings



###########################

# setup functions
# we dont change them directly (if u wanna change smth, edit config stuff)
def loadConfig(configfile):
    global network, token, gasprice, _chainid, pendingBalances, pendingBalancesToken, abi, wrapperUsername, wrapperPassword, config
    file = open(configfile, "r")
    config = json.load(file)
    file.close()
    wrapperUsername = config["username"]
    wrapperPassword = config["password"]
    _chainid = config["chainid"]
    config["address"] = eth_account.Account.privateKeyToAccount(config["privateKey"]).address
    config["privateKey"] = bytes.fromhex(config["privateKey"])
    print(f"Server address : {config['address']}")

loadConfig(_configLocation)

def setupChain(chainid, contractAddress, _gasprice, rpc):
    global network, token, gasprice, _chainid, pendingBalances, pendingBalancesToken, abi
    network[chainid] = Web3(Web3.HTTPProvider(rpc))
    gasprice[chainid] = _gasprice
    token[chainid] = network[chainid].eth.contract(address=contractAddress, abi=abi)

setupChain(56, "0xCF572cA0AB84d8Ce1652b175e930292E2320785b", 5000000000, "https://bsc-dataseed3.binance.org")
setupChain(97, Web3.toChecksumAddress("0x911f311dfff09680adc3a433e03c57e2cb4945b2"), 10000000000, "https://data-seed-prebsc-1-s1.binance.org:8545")


def loadDB():
    global network, token, gasprice, _chainid, pendingBalances, pendingBalancesToken, abi, wrapperUsername, wrapperPassword, alreadyProcessed, config
    try:
        file = open(config["dataBaseFile"], "r")
        file.seek(0)
        db = json.load(file)
        file.close()
        alreadyProcessed = db["transactions"]
        pendingBalances = db["pendingBalances"]
        pendingBalancesToken = db["pendingBalancesToken"]
    except Exception as e:
        alreadyProcessed = []
        pendingBalances = {}
        pendingBalancesToken = {}
        print(e)

def saveDB():
    global network, token, gasprice, _chainid, pendingBalances, pendingBalancesToken, abi, wrapperUsername, wrapperPassword, alreadyProcessed, config
    db = {"transactions": alreadyProcessed, "pendingBalances":pendingBalances, "pendingBalancesToken": pendingBalancesToken}
    db = str(db).replace("\'", "\"")
    file = open(config["dataBaseFile"], "w")
    file.write(db)
    file.close()


loadDB()
###########################
# Token related functions


def isValid(address):
    try:
        Web3.toChecksumAddress(address)
    except:
        return False
    else:
        return True

def processWithdawToken(address, amount):
    global network, token, gasprice, config, _chainid
    try:        
        _network = network[_chainid]
        tx = token[_chainid].functions.wrap(address, int(float(amount)*(10**18))).buildTransaction({'nonce': network[_chainid].eth.get_transaction_count(config["address"]),'chainId': _chainid, 'gasPrice': gasprice[_chainid], 'from':config["address"]})
        tx = _network.eth.account.sign_transaction(tx, config["privateKey"])
        txid = _network.toHex(_network.keccak(tx.rawTransaction))
        print("txid :",txid)
        _network.eth.send_raw_transaction(tx.rawTransaction)
        receipt = _network.eth.waitForTransactionReceipt(txid)
        if receipt['status'] == 0:
            return False
        else:
            return True
    except:
        return False


def processDepositToken(username, address, amount):
    global network, token, gasprice, config, _chainid
    try:
        _network = network[_chainid]
        tx = token[_chainid].functions.confirmWithdraw(username, address, int(float(amount)*(10**18))).buildTransaction({'nonce': network[_chainid].eth.get_transaction_count(config["address"]),'chainId': _chainid, 'gasPrice': gasprice[_chainid], 'from':config["address"]})
        tx = _network.eth.account.sign_transaction(tx, config["privateKey"])
        txid = _network.toHex(_network.keccak(tx.rawTransaction))
        print("txid :",txid)
        _network.eth.send_raw_transaction(tx.rawTransaction)
        receipt = _network.eth.waitForTransactionReceipt(txid)
        if receipt['status'] == 0:
            return False
        else:
            return True
    except:
        return False

def cancelDepositToken(username, address):
    global network, token, gasprice, config, _chainid
    try:
        _network = network[_chainid]
        tx = token[_chainid].functions.cancelWithdrawals(address, username).buildTransaction({'nonce': network[_chainid].eth.get_transaction_count(config["address"]),'chainId': _chainid, 'gasPrice': gasprice[_chainid], 'from':config["address"]})
        tx = _network.eth.account.sign_transaction(tx, config["privateKey"])
        txid = _network.toHex(_network.keccak(tx.rawTransaction))
        print("txid :",txid)
        _network.eth.send_raw_transaction(tx.rawTransaction)
        receipt = _network.eth.waitForTransactionReceipt(txid)
        if receipt['status'] == 0:
            return False
        else:
            return True
    except:
        return False


def withdrawToWrapped(address):
    global _chainid, pendingBalancesToken
    amount = float(pendingBalancesToken[address])
    pendingBalancesToken[address] = 0
    feedback = processWithdawToken(address, amount)
    if not feedback:
        pendingBalancesToken[address] = amount
    saveDB()

def checkDepositsToken():
    global pendingBalances, _chainid, token
    users = token[_chainid].functions.getUserList().call()
    for i in range(len(users)):
        user = users[i]
        pendingUnwraps = user[2]/10**18
        if pendingUnwraps > 0:
            receipt = processDepositToken(user[1], user[0], pendingUnwraps)
            if receipt:
                pendingBalances[user[1]] = (pendingBalances.get(user[1]) or 0) + pendingUnwraps
    saveDB()




#####################################
# DUCO network functions

def checkDepositsDuco():
    global pendingBalancesToken, alreadyProcessed
    txs = requests.get("https://server.duinocoin.com/transactions").json()
    for key, value in txs["result"].items():
        if value["recipient"] == wrapperUsername and not (key in alreadyProcessed):
            alreadyProcessed += [key]
            if (isValid(value["memo"])):
                pendingBalancesToken[Web3.toChecksumAddress(value["memo"])] = (pendingBalancesToken.get(Web3.toChecksumAddress(value["memo"])) or 0) + value["amount"]
                print(f"Deposit received, address : {Web3.toChecksumAddress(value['memo'])}, txid : {key}")
            else:
                pendingBalances[value["sender"]] = (pendingBalancesToken.get(value["sender"]) or 0) + value["amount"]
            saveDB()
    saveDB()

def processWithdraw(username):
    if (pendingBalances[username] > 0):
        _amount = pendingBalances[username]
        pendingBalances[username] = 0
        usernameMemo = username.split(",")
        socket = Wallet()
        socket.login(username=wrapperUsername, password=wrapperPassword)
        feedback = socket.transfer(recipient_username=usernameMemo[0], amount=_amount, memo=usernameMemo[1])
        print(feedback)
        if "NO" in feedback:
            pendingBalances[username] = _amount
    saveDB()


###################################
# stuff for processing all at once 
def processAllWithdrawalsToken():
    global _chainid
    for key, value in pendingBalancesToken.items():
        if float(value) > 0:
            withdrawToWrapped(key)


def processAllWithdrawals():
    global _chainid
    for key, value in pendingBalances.items():
        if float(value) > 0:
            processWithdraw(key)



###################################
# Loop in order to refresh constantly and process stuff
while True:
    checkDepositsDuco()
    checkDepositsToken()
    processAllWithdrawals()
    processAllWithdrawalsToken()
    time.sleep(15)