import requests, time, json, eth_account, os
from duco_api import Wallet
from web3 import Web3

abi = """[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"}],"name":"RevokeWrapper","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":true,"internalType":"string","name":"_ducoUsername","type":"string"}],"name":"UnwrapConfirmed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":true,"internalType":"string","name":"_ducoUsername","type":"string"}],"name":"UnwrapInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"Wrap","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_address","type":"address"}],"name":"allowWrapper","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_oldAdmin","type":"address"},{"indexed":true,"internalType":"address","name":"_newAdmin","type":"address"}],"name":"changeAdminConfirmed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_currentAdmin","type":"address"},{"indexed":true,"internalType":"address","name":"_newAdmin","type":"address"}],"name":"changeAdminRequest","type":"event"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"ChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"addWrapperAccess","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cancelChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"_ducousername","type":"string"}],"name":"cancelWithdrawals","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"checkWrapperStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"confirmChangeAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_ducousername","type":"string"},{"internalType":"address","name":"_address","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"confirmWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentAdmin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getUserList","outputs":[{"components":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"username","type":"string"},{"internalType":"uint256","name":"pendingBalance","type":"uint256"}],"internalType":"struct ERC20.addressUsername[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_ducousername","type":"string"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"initiateWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"_ducousername","type":"string"}],"name":"pendingWithdrawals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"","type":"bytes"}],"name":"positionInList","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"revokeWrapperAccess","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"","type":"bytes"}],"name":"userExists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"usersList","outputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"string","name":"username","type":"string"},{"internalType":"uint256","name":"pendingBalance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"usersListLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tronaddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"wrap","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]"""


class Wrapper(object):
    def __init__(self, _configLocation):
        self.gasprice = {}
        self.network = {}
        self.token = {}
        self.configLocation = _configLocation
        self.alreadyProcessed = []
        self.pendingBalances = {}
        self.refunds = []
        self.wrapFee = 500
        
        self.loadChains()
        self.loadConfig(self.configLocation)
        self.loadDB()

    ###########################

    # setup functions
    # we dont change them directly (if u wanna change smth, edit config stuff)
    def loadConfig(self, configfile):
        file = open(configfile, "r")
        self.config = json.load(file)
        file.close()
        self.wrapperUsername = self.config["username"]
        self.wrapperPassword = self.config["password"]
        self.chainid = self.config["chainid"]
        try:
            _shallUseApi = self.config["apifortxs"]
        except Exception as e:
            print(e)
            _shallUseApi = False
            print("Using socket for sending transactions")
        if (_shallUseApi):
            print("Using API for sending transactions")
        else:
            print("Using socket for sending transactions")
        self.config["apifortxs"] = _shallUseApi
        self.config["address"] = eth_account.Account.privateKeyToAccount(self.config["privateKey"]).address
        self.config["privateKey"] = bytes.fromhex(self.config["privateKey"])
        print(f"Server address : {self.config['address']}")

    def setupChain(self, chainid, contractAddress, _gasprice, rpc):
        _protocol_ = rpc.split(":")[0]
        if ((_protocol_ == "https") or (_protocol_ == "http")):
            self.network[chainid] = Web3(Web3.HTTPProvider(rpc))
        elif ((_protocol_ == "wss") or (_protocol_ == "ws")):
            self.network[chainid] = Web3(Web3.WebsocketProvider(rpc))
        self.gasprice[chainid] = _gasprice
        self.token[chainid] = self.network[chainid].eth.contract(address=contractAddress, abi=abi)


    def loadChains(self):
        chainsfile = open("chains.json", "r")
        chains = json.load(chainsfile)
        chainsfile.close()
        for key, value in chains.items():
            self.setupChain(int(key), value["contract"], value["gas"]*(10**9), value["rpc"])

    def gasPrice(chainid):
        try:
            gasapi = self.chains[str(chainid)]["gasapi"]
            return int(min(requests.get(gasapi).json()["fast"], self.chains[str(chainid)]["gas"])*self.config["gasMultiplier"])
        except:
            return int(int(self.gasprice[chainid])*self.config["gasMultiplier"])


    def loadDB(self):
        try:
            file = open(self.config["dataBaseFile"], "r")
            file.seek(0)
            db = json.load(file)
            file.close()
            self.alreadyProcessed = db["transactions"]
            self.pendingBalances = db["pendingBalances"]
            self.pendingBalancesToken = db["pendingBalancesToken"]
        except Exception as e:
            self.alreadyProcessed = []
            self.pendingBalances = {}
            self.pendingBalancesToken = {}
            print(e)

    def saveDB(self):
        db = {"transactions": self.alreadyProcessed, "pendingBalances": self.pendingBalances, "pendingBalancesToken": self.pendingBalancesToken}
        db = str(db).replace("\'", "\"")
        file = open(self.config["dataBaseFile"], "w")
        file.write(db)
        file.close()

    ###########################
    # Checkpoint stuff (beta)

    def saveCheckpoint(self):
        try:
            pathToCheckpoint = self.config['checkPointPath']
            _dbfile = self.config['dataBaseFile']
            if pathToCheckpoint:
                result = os.system(f"cp -r {_dbfile} {pathToCheckpoint}")    # copies DB file to remote (rclone-mounted) directory
                if (result == 0):
                    print("Successfully saved checkpoint !")
                else:
                    print("Error saving checkpoint...")
        except Exception as e:
            print(e)

    ###########################
    # Token related functions


    def isValid(self, address):
        try:
            Web3.toChecksumAddress(address)
        except:
            return False
        else:
            return True

    def processWithdawToken(self, address, amount):
        try:
            _network = self.network[self.chainid]
            _nonce_ = self.network[self.chainid].eth.get_transaction_count(self.config["address"])
            tx = self.token[self.chainid].functions.wrap(address, int(float(amount)*(10**18))).buildTransaction({'nonce': _nonce_,'chainId': self.chainid, 'gasPrice': self.gasPrice(self.chainid), 'from':self.config["address"]})
            tx = _network.eth.account.sign_transaction(tx, self.config["privateKey"])
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


    def processDepositToken(self, username, address, amount):
        try:
            _network = self.network[self.chainid]
            tx = self.token[self.chainid].functions.confirmWithdraw(username, address, min(self.token[self.chainid].functions.pendingWithdrawals(address, username).call(),int(float(amount)*(10**18)))).buildTransaction({'nonce': self.network[self.chainid].eth.get_transaction_count(self.config["address"]),'chainId': self.chainid, 'gasPrice': self.gasPrice(self.chainid), 'from':self.config["address"]})
            tx = _network.eth.account.sign_transaction(tx, self.config["privateKey"])
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

    def cancelDepositToken(self, username, address):
        try:
            _network = self.network[self.chainid]
            tx = self.token[self.chainid].functions.cancelWithdrawals(address, username).buildTransaction({'nonce': self.network[self.chainid].eth.get_transaction_count(config["address"]),'chainId': self.chainid, 'gasPrice': self.gasPrice(self.chainid), 'from':self.config["address"]})
            tx = _network.eth.account.sign_transaction(tx, self.config["privateKey"])
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


    def withdrawToWrapped(self, address):
        amount = float(self.pendingBalancesToken[address])
        print(f"Withdrawing {amount} to {address}")
        del self.pendingBalancesToken[address]
        feedback = self.processWithdawToken(address, amount)
        print(f"feedback : {feedback}")
        if ((not feedback[0]) and (not feedback[1])):
            self.pendingBalancesToken[address] = amount # refund if wrapper encounters exception at sending step
        elif (feedback[1]):
            erroredTx = feedback[1]                     # notice to dev if transaction remains pending (but sending succeeds)
            self.refunds.append(erroredTx);
        self.saveDB()

    def checkRefunds(self):
        errorsfile = open("errors.err", "a")
        for erroredTx in self.refunds:
            try:
                receipt = self.networks[self.chainid].eth.waitForTransactionReceipt(erroredTx["tx"])
                print(f"Tx {erroredTx['tx']} exists on chain, not gonna refund anything !")
            except:
                errorsfile.write(f"{erroredTx['txid']} : {erroredTx['tokens']} to {erroredTx['to']}\n")
        errorsfile.close()
        self.refunds = []

    def userExists(self, _username):
        return requests.get(f"https://server.duinocoin.com/users/{_username}").json().get("success")

    def checkDepositsToken(self):
        users = self.token[self.chainid].functions.getUserList().call()
        for user in users:
            if (user[1].split(",")[0] != wrapperUsername):  # ensures unwrap goes to someone else
                pendingUnwraps = user[2]/10**18             # token decimals
                fees = (pendingUnwraps*config["fee"])/100   # unwrap fee in percents
                unwrapWithoutFees = pendingUnwraps - fees
                if (pendingUnwraps > 0 and self.userExists(user[1].split(',')[0])):  # ensures recipient exists
                    receipt = self.processDepositToken(user[1], user[0], pendingUnwraps)
                    if receipt:
                        self.pendingBalances[user[1]] = self.pendingBalances.get(user[1], 0) + unwrapWithoutFees
                        self.pendingBalances[config["feeRecipient"]] = pendingBalances.get(config["feeRecipient"], 0) + fees
            else:
                if (user[2] > 0):
                    self.cancelDepositToken(user[1], user[0])   # cancel unwrap if it goes to bscDUCO wrapper
        self.saveDB()




    #####################################
    # DUCO network functions
    def txlistToMapping(self, _list):
        returnValue = {}
        for i in _list:
            try:
                returnValue[i["hash"]] = i
            except:
                pass    # ignore if unable to extract hash
        return returnValue

    def checkDepositsDuco(self, forceRecheck):
        _feeRecipient = self.config["feeRecipient"]
        txs = requests.get("https://server.duinocoin.com/transactions").json()["result"] if forceRecheck else txlistToMapping(requests.get(f"https://server.duinocoin.com/users/{wrapperUsername}").json()["result"]["transactions"])
        for key, value in txs.items():
            if ((value["recipient"] == wrapperUsername) and (not (key in self.alreadyProcessed))):  # ensure DUCO-side recipient is wrapper AND transaction hasn't already been processed
                self.alreadyProcessed.append(key)
                if ((self.isValid(value["memo"])) and (int(value["amount"]) >= self.wrapFee)):   # ensures evm-side recipient address is valid and amount is sufficient to cover wrap fees
                    _addr = Web3.toChecksumAddress(value["memo"])
                    self.pendingBalancesToken[_addr] = self.pendingBalancesToken.get(_addr, 0) + (value["amount"] - self.wrapFee)
                    self.pendingBalances[_feeRecipient] = self.pendingBalances.get(_feeRecipient, 0) + self.wrapFee
                    print(f"Deposit received, address : {_addr}, txid : {key}")
                elif ((value["memo"] == "burn") or ("staking" in value["memo"].lower())):
                    pass
                else:
                    self.pendingBalances[value["sender"]] = self.pendingBalances.get(value["sender"], 0) + value["amount"]
                    self.saveDB()
        self.saveDB()

    def processWithdraw(self, username):
        if (self.pendingBalances[username] > 0):
            _amount = self.pendingBalances[username]
            try:
                print(f"Withdrawing {_amount} to {username}")
                del self.pendingBalances[username]  # deleting is more storage-efficient than setting to zero
                usernameMemo = username.split(",")
                _username = usernameMemo[0].replace('&', '').replace('?', '')
                _memo = usernameMemo[1].replace('&', '').replace('?', '') if (len(usernameMemo) > 1) else "-"
                if not self.userExists(_username):
                    print(f"User {_username} does not exist, ignoring...")
                    return # skips rest of function, erases pending balance
                if (self.config["apifortxs"]):
                    feedbacka = requests.get(f"https://server.duinocoin.com/transaction/?username={self.wrapperUsername}&password={self.wrapperPassword}&recipient={_username}&amount={_amount}&memo={_memo}").json()
                    print(feedbacka)
                    feedback = feedbacka["result"]
                else:
                    socket = Wallet()
                    socket.login(username=self.wrapperUsername, password=self.wrapperPassword)
                    feedback = socket.transfer(recipient_username=_username, amount=_amount, memo=_memo)
                    socket.logout()
                print(feedback)
                if not "OK" in feedback:
                    self.pendingBalances[username] = _amount # revert in case of transaction error
            except Exception as e:
                print(e)
                self.pendingBalances[username] = _amount     # revert in case of exception
        self.saveDB()


    ###################################
    # stuff for processing all at once
    def processAllWithdrawalsToken(self):
        for key, value in self.pendingBalancesToken.items():
            if float(value) > 0:
                self.withdrawToWrapped(key)


    def processAllWithdrawals():
        for key, value in self.pendingBalances.items():
            if float(value) > 0:
                self.processWithdraw(key)



    ###################################
    # Loop in order to refresh constantly and process stuff
    def looping(self):
        n = 0
        while True:
            try:
        #        checkDepositsDuco(n%10 == 0)
                self.checkDepositsDuco(False)
            except Exception as e:
                print(e)
            try:
               self.checkDepositsToken()
            except Exception as e:
                print(e)
            try:
                self.processAllWithdrawals()
            except Exception as e:
                print(e)
            try:
                self.processAllWithdrawalsToken()
            except Exception as e:
                print(e)
            try:
                self.checkRefunds()
            except Exception as e:
                print(e)
            if (n%500 == 0):
                self.saveCheckpoint()
            n += 1
            time.sleep(30)