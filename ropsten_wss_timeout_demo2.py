#shows web3.py works when toBlock - fromBlock <= 112, but timeout when toBlock - fromBlock > 112
import os
import sys
import json
from collections import OrderedDict

import web3
from web3.providers import WebsocketProvider


PROJECT_ID = os.environ.get('PROJECT_ID') or '' # Infura Project ID
if not PROJECT_ID:
    print('Error: env variable PROJECT_ID not found', file=sys.stderr)
    sys.exit(1)

ROPSTEN_ENDPOINT = f'wss://ropsten.infura.io/ws/v3/{PROJECT_ID}'

WEBSOCKET_TIMEOUT = 30 # raising timeout makes no difference
ABI_FILEPATH = 'ABI_Ropsten.json'

with open(ABI_FILEPATH, 'r', encoding='utf-8') as abi_file:
    abi_json = json.loads(abi_file.read())
    Contract_Address = web3.Web3.toChecksumAddress(abi_json["contractAddress"].lower())
    contract_abi = abi_json['abi']

w3 = web3.Web3(WebsocketProvider(ROPSTEN_ENDPOINT, websocket_timeout=WEBSOCKET_TIMEOUT))
contract = w3.eth.contract(address=Contract_Address, abi=contract_abi)

tests = OrderedDict() # {from_block: message}
tests[6807400] = 'works when toBlock-fromBlock <= 112, timeout when toBlock-fromBlock > 112'

for from_block, msg in tests.items():
    print(f'fromBlock={from_block}, {msg}', flush=True)

    print('when toBlock-fromBlock <= 112')
    event_filter = contract.events.EthUpdate.createFilter(fromBlock=from_block, toBlock=from_block+112)
    all_entries = event_filter.get_all_entries()
    for event in all_entries[:2]:
        print(f'EthUpdate event transactionHash {event.transactionHash.hex()}', flush=True)
    print()

    print('when toBlock-fromBlock > 112')
    event_filter = contract.events.EthUpdate.createFilter(fromBlock=from_block, toBlock=from_block+113)
    all_entries = event_filter.get_all_entries()
    for event in all_entries[:3]:
        print(f'EthUpdate event transactionHash {event.transactionHash.hex()}', flush=True)
