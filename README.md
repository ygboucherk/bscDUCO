# bscDUCO
BscDUCO is a token that allows transferring duino-coin (the only arduino-mineable cryptocurrency) to Binance Smart Chain (BSC) for pancakeswap trades and more stuff.


### How does that work ?
For each circulating bscDUCO, one DUCO is stored in [a custody account](https://explorer.duinocoin.com/?search=bscDUCO).

Token address : [0xcf572ca0ab84d8ce1652b175e930292e2320785b](https://bscscan.com/token/0xcf572ca0ab84d8ce1652b175e930292e2320785b)

Custody account : [bscDUCO](https://explorer.duinocoin.com/?search=bscDUCO)


### How to get bscDUCO ?
If you send DUCO to custody account (bscDUCO) and use your bsc address as memo, transaction will be automatically processed !

*note: Tech is still in beta and could lead to loss of funds, don't wrap too big amounts !!!*

### How to get back DUCO ?
Feel free to visit [the unwrapping dApp](https://bsc.duinocoin.com/) in order to unwrap them !


## Other chains
As this system can easily be ported to other EVM chains, we can have duco almost everywhere !

It uses same custody system but different config !!!

[Wrap/nbwrap dApp](https://bsc.duinocoin.com/) automatically detects when metmask is connected to another network, and will automatically switch token !

### Polygon
Custody account : [maticDUCO](https://explorer.duinocoin.com/?search=maticDUCO)

Token : [0xaf965beb8c830ae5dc8280d1c7215b8f0acc0cea](https://polygonscan.com/token/0xaf965beb8c830ae5dc8280d1c7215b8f0acc0cea)

### Celo
Custody account : [celoDUCO](https://explorer.duinocoin.com/?search=celoDUCO)

Token : [0xDB452CC669D3Ae454226AbF232Fe211bAfF2a1F9](https://explorer.celo.org/tokens/0xDB452CC669D3Ae454226AbF232Fe211bAfF2a1F9/)

### RaptorChain
Custody account : [rDUCO](https://explorer.duinocoin.com/?search=rDUCO)

Token : [0x9ffE5c6EB6A8BFFF1a9a9DC07406629616c19d32](https://explorer.raptorchain.io/address/0x9ffE5c6EB6A8BFFF1a9a9DC07406629616c19d32/)


### More chains are planned in the future (like harmony) !


## Some other stuff
In-custody DUCO shall always be more or equal to token's supply. If custody is below token's supply, that means tokens are unbacked (we are not tether), and and please raise an issue immediately !
