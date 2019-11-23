# Shows Infura Ropsten websocket timeout in web3.py, but not in web3.js


## Prerequisites

```bash
pip3 install -r requirements.txt

npm install
```

```bash
export PROJECT_ID=<Your Infura Project ID>
```


## Run

Same implementation, returns events in web3.js, timeout in web3.py --

```bash
node ropstenWssTimeoutDemo.js

python3 ropsten_wss_timeout_demo.py
```

In addition, ropsten_wss_timeout_demo2.py shows timeout behavior difference within web3.py for from_block just 100 apart --

```bash
python3 ropsten_wss_timeout_demo2.py
```

* Note: The two events, EthUpdate and BrickTransfer, are generated from the same function
