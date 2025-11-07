import requests, time, json, eth_account, os
global network, token, gasprice, _chainid, pendingBalances, pendingBalancesToken, abi, wrapperUsername, wrapperPassword, alreadyProcessed, config, currentBalance, wrapFee
from duco_api import Wallet
from web3 import Web3


gasprice = {}
network = {}
token = {}

_configLocation = "wrapperConfig.json"



abi = """[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"}],"name":"RevokeWrapper","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":true,"internalType":"string","name":"_ducoUsername","type":"string"}],"name":"UnwrapConfirmed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":true,"internalType":"string","name":"_ducoUsername","type":"string"}],"name":"UnwrapInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"Wrap","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"}],"name":"allowWrapper","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_oldAdmin","type":"address"},{"indexed":true,"internalType":"address","name":"_newAdmin","type":"address"}],"name":"changeAdminConfirmed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_currentAdmin","type":"address"},{"indexed":true,"internalType":"address","name":"_newAdmin","type":"address"}],"name":"changeAdminRequest","type":"event"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"ChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"addWrapperAccess","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cancelChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"_ducousername","type":"string"}],"name":"cancelWithdrawals","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"checkWrapperStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"confirmChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_ducousername","type":"string"},{"internalType":"address","name":"_address","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"confirmWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentAdmin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getUserList","outputs":[{"components":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"username","type":"string"},{"internalType":"uint256","name":"pendingBalance","type":"uint256"}],"internalType":"struct ERC20.addressUsername[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_ducousername","type":"string"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"initiateWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"_ducousername","type":"string"}],"name":"pendingWithdrawals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"","type":"bytes"}],"name":"positionInList","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"revokeWrapperAccess","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"","type":"bytes"}],"name":"userExists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"usersList","outputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"username","type":"string"},{"internalType":"uint256","name":"pendingBalance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"usersListLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tronaddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"wrap","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]"""

alreadyProcessed = []
pendingBalances = {} # good old mappings
currentBalance = 0
refunds = []
wrapFee = 500

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
    try:
        _shallUseApi = config["apifortxs"]
    except Exception as e:
        print(e)
        _shallUseApi = False
        print("Using socket for sending transactions")
    if (_shallUseApi):
        print("Using API for sending transactions")
    else:
        print("Using socket for sending transactions")
    config["apifortxs"] = _shallUseApi
    config["address"] = eth_account.Account.privateKeyToAccount(config["privateKey"]).address
    config["privateKey"] = bytes.fromhex(config["privateKey"])
    print(f"Server address : {config['address']}")

loadConfig(_configLocation)

def setupChain(chainid, contractAddress, _gasprice, rpc):
    global network, token, gasprice, _chainid, pendingBalances, pendingBalancesToken, abi
    _protocol_ = rpc.split(":")[0]
    if ((_protocol_ == "https") or (_protocol_ == "http")):
        network[chainid] = Web3(Web3.HTTPProvider(rpc))
    elif ((_protocol_ == "wss") or (_protocol_ == "ws")):
        network[chainid] = Web3(Web3.WebsocketProvider(rpc))
    gasprice[chainid] = _gasprice
    token[chainid] = network[chainid].eth.contract(address=contractAddress, abi=abi)

chainsfile = open("chains.json", "r")
chains = json.load(chainsfile)
chainsfile.close()
for key, value in chains.items():
    setupChain(int(key), value["contract"], value["gas"]*(10**9), value["rpc"])

def gasPrice(chainid):
    try:
        gasapi = chains[str(chainid)]["gasapi"]
        return int(min(requests.get(gasapi).json()["fast"], chains[str(chainid)]["gas"])*config["gasMultiplier"])
    except:
        return int(int(gasprice[chainid])*config["gasMultiplier"])


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
# Checkpoint stuff (beta)

def saveCheckpoint():
    try:
        pathToCheckpoint = config['checkPointPath']
        if pathToCheckpoint:
            result = os.system(f"cp -r {config['dataBaseFile']} {pathToCheckpoint}")
            if (result == 0):
                print("Successfully saved checkpoint !")
            else:
                print("Error saving checkpoint...")
    except Exception as e:
        print(e)

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
        _nonce_ = network[_chainid].eth.get_transaction_count(config["address"])
        tx = token[_chainid].functions.wrap(address, int(float(amount)*(10**18))).buildTransaction({'nonce': _nonce_,'chainId': _chainid, 'gasPrice': gasPrice(_chainid), 'from':config["address"]})
        tx = _network.eth.account.sign_transaction(tx, config["privateKey"])
        txid = _network.toHex(_network.keccak(tx.rawTransaction))
        print("txid :",txid)
        _network.eth.send_raw_transaction(tx.rawTransaction)
        receipt = _network.eth.wait_for_transaction_receipt(txid, timeout=120)
        print(receipt)
        if receipt['status'] == 0:
            return (False, False)
        else:
            return (True,False)
    except Exception as e:
        try:
            returnValue = (False,{"tx": txid, "tokens": amount, "to": address, "nonce": _nonce_})
        except:
            returnValue = (False, False)
            print("Error marking failed TX, returning False")
        print(e)
        return returnValue


def processDepositToken(username, address, amount):
    global network, token, gasprice, config, _chainid
    try:
        _network = network[_chainid]
        tx = token[_chainid].functions.confirmWithdraw(username, address, min(token[_chainid].functions.pendingWithdrawals(address, username).call(),int(float(amount)*(10**18)))).buildTransaction({'nonce': network[_chainid].eth.get_transaction_count(config["address"]),'chainId': _chainid, 'gasPrice': gasPrice(_chainid), 'from':config["address"]})
        tx = _network.eth.account.sign_transaction(tx, config["privateKey"])
        txid = _network.toHex(_network.keccak(tx.rawTransaction))
        print("txid :",txid)
        _network.eth.send_raw_transaction(tx.rawTransaction)
        receipt = _network.eth.wait_for_transaction_receipt(txid)
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
        tx = token[_chainid].functions.cancelWithdrawals(address, username).buildTransaction({'nonce': network[_chainid].eth.get_transaction_count(config["address"]),'chainId': _chainid, 'gasPrice': gasPrice(_chainid), 'from':config["address"]})
        tx = _network.eth.account.sign_transaction(tx, config["privateKey"])
        txid = _network.toHex(_network.keccak(tx.rawTransaction))
        print("txid :",txid)
        _network.eth.send_raw_transaction(tx.rawTransaction)
        receipt = _network.eth.waitForTransactionReceipt(txid)
        if receipt['status'] == 0:
            return False
        else:
            return True
    except Exception as e:
        print(e)
        return False


def withdrawToWrapped(address):
    global _chainid, pendingBalancesToken, refunds
    amount = float(pendingBalancesToken[address])
    print(f"Withdrawing {amount} to {address}")
    pendingBalancesToken[address] = 0
    feedback = processWithdawToken(address, amount)
    print(f"feedback : {feedback}")
    if ((not feedback[0]) and (not feedback[1])):
        pendingBalancesToken[address] = amount
    elif (feedback[1]):
        erroredTx = feedback[1]
        refunds.append(erroredTx);
    saveDB()

def checkRefunds():
    global _chainid, pendingBalancesToken, refunds
    errorsfile = open("errors.err", "a")
    for erroredTx in refunds:
        try:
            receipt = _network.eth.waitForTransactionReceipt(erroredTx["tx"])
            print(f"Tx {erroredTx['tx']} exists on chain, not gonna refund anything !")
        except:
            errorsfile.write(f"{erroredTx['txid']} : {erroredTx['tokens']} to {erroredTx['to']}\n")
#            pendingBalancesToken[erroredTx["to"]] += erroredTx["tokens"]
#            print(f"Tx {erroredTx['tx']} not found, re-added {erroredTx['tokens']}")
    errorsfile.close()
    refunds = []

def checkDepositsToken():
    global pendingBalances, _chainid, token
    users = token[_chainid].functions.getUserList().call()
    for user in users:
        if (user[1].split(",")[0] != wrapperUsername):
            pendingUnwraps = user[2]/10**18
            fees = (pendingUnwraps*config["fee"])/100
            unwrapWithoutFees = pendingUnwraps - fees
#            if user[2]:
 #               print(user)
            try:
                if pendingUnwraps > 0 and (requests.get(f"https://server.duinocoin.com/users/{user[1].split(',')[0]}").json().get("success")):
                    receipt = processDepositToken(user[1], user[0], pendingUnwraps)
                    if receipt:
                        pendingBalances[user[1]] = (pendingBalances.get(user[1]) or 0) + unwrapWithoutFees
                        pendingBalances[config["feeRecipient"]] = (pendingBalances.get(config["feeRecipient"]) or 0) + fees
            except Exception as e:
                print(repr(e))
        else:
            if (user[2] > 0):
                cancelDepositToken(user[1], user[0])
    saveDB()




#####################################
# DUCO network functions
def txlistToMapping(_list):
    returnValue = {}
    for i in _list:
        returnValue[i["hash"]] = i
    return returnValue

def checkDepositsDuco(forceRecheck):
    global pendingBalancesToken, alreadyProcessed, currentBalance, wrapFee
    if (forceRecheck):
        txs = requests.get("https://server.duinocoin.com/transactions").json()["result"]
    else:
        txs = txlistToMapping(requests.get(f"https://server.duinocoin.com/users/{wrapperUsername}").json()["result"]["transactions"])
    for key, value in txs.items():
        if ((value["recipient"] == wrapperUsername) and (not (key in alreadyProcessed))):
            alreadyProcessed += [key]
            if ((isValid(value["memo"])) and (int(value["amount"]) >= wrapFee)):
                pendingBalancesToken[Web3.toChecksumAddress(value["memo"])] = (pendingBalancesToken.get(Web3.toChecksumAddress(value["memo"])) or 0) + (value["amount"] - wrapFee)
                pendingBalances[config["feeRecipient"]] = (pendingBalances.get(config["feeRecipient"]) or 0) + wrapFee
                print(f"Deposit received, address : {Web3.toChecksumAddress(value['memo'])}, txid : {key}")
            elif ((value["memo"] == "burn") or ("staking" in value["memo"].lower())):
                pass
            else:
                pendingBalances[value["sender"]] = (pendingBalancesToken.get(value["sender"]) or 0) + value["amount"]
                saveDB()
    saveDB()

def processWithdraw(username):
    if (pendingBalances[username] > 0):
        _amount = pendingBalances[username]
        try:
            print(f"Withdrawing {_amount} to {username}")
            pendingBalances[username] = 0
            usernameMemo = username.split(",")
            _username = usernameMemo[0]
            try:
                _memo = usernameMemo[1]
            except:
                _memo = "-"
            if (config["apifortxs"]):
                feedbacka = requests.get(f"https://server.duinocoin.com/transaction/?username={wrapperUsername}&password={wrapperPassword}&recipient={_username.replace('&', '')}&amount={_amount}&memo={_memo}").json()
                print(feedbacka)
                feedback = feedbacka["result"]
            else:
                socket = Wallet()
                socket.login(username=wrapperUsername, password=wrapperPassword)
                feedback = socket.transfer(recipient_username=_username, amount=_amount, memo=_memo)
                socket.logout()
            print(feedback)
            if not "OK" in feedback:
                pendingBalances[username] = _amount
        except Exception as e:
            print(e)
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
n = 0
while True:
    try:
        checkDepositsDuco(n%60 == 0)
    except Exception as e:
        print(e)
    try:
       checkDepositsToken()
    except Exception as e:
        print(e)
    try:
        processAllWithdrawals()
    except Exception as e:
        print(e)
    try:
        processAllWithdrawalsToken()
    except Exception as e:
        print(e)
    try:
        checkRefunds()
    except Exception as e:
        print(e)
    if (n%500 == 0):
        saveCheckpoint()
    n += 1
    time.sleep(30)
