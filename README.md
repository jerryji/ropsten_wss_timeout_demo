# Shows Infura Ropsten websocket timeout (with web3.py)


## Prerequisites

```bash
pip3 install -r requirements.txt
```

```bash
export PROJECT_ID=...
```


## Run

```bash
python3 ropsten_wss_timeout_demo.py
```


## Output

```
fromBlock=6807500, Both BrickTransfer and EthUpdate succeed
BrickTransfer event transactionHash 0xee9fffbf547c2aed22df404c5a9ee247fb030f92027c18a08f2532fb8d1c60ef
BrickTransfer event transactionHash 0xee9fffbf547c2aed22df404c5a9ee247fb030f92027c18a08f2532fb8d1c60ef
BrickTransfer event transactionHash 0xee9fffbf547c2aed22df404c5a9ee247fb030f92027c18a08f2532fb8d1c60ef

EthUpdate event transactionHash 0xee9fffbf547c2aed22df404c5a9ee247fb030f92027c18a08f2532fb8d1c60ef
EthUpdate event transactionHash 0xee9fffbf547c2aed22df404c5a9ee247fb030f92027c18a08f2532fb8d1c60ef
EthUpdate event transactionHash 0xee9fffbf547c2aed22df404c5a9ee247fb030f92027c18a08f2532fb8d1c60ef

fromBlock=6807400, BrickTransfer succeeds, but EthUpdate will timeout
BrickTransfer event transactionHash 0xb0e40b17a73fc8fd32b80e90b18257d490c96328fe55d3a7514276bff888ab19
BrickTransfer event transactionHash 0xb0e40b17a73fc8fd32b80e90b18257d490c96328fe55d3a7514276bff888ab19
BrickTransfer event transactionHash 0xb0e40b17a73fc8fd32b80e90b18257d490c96328fe55d3a7514276bff888ab19

```
